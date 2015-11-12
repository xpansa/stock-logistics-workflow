# -*- coding: utf-8 -*-
# © 2015 Xpansa Group
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from openerp import api, fields, models


class StockMove(models.Model):
    _inherit = 'stock.move'

    @api.one
    @api.depends('product_id')
    def _compute_locations_with_product(self):
        if not self.product_id or not self.location_id:
            return

        warehouse_root_locations = []
        warehouse_model = self.env['stock.warehouse']
        warehouses = warehouse_model.search([])
        for warehouse in warehouses:
            warehouse_root_locations.append(warehouse.wh_input_stock_loc_id.id)
            warehouse_root_locations.append(
                warehouse.wh_output_stock_loc_id.id)
            warehouse_root_locations.append(warehouse.lot_stock_id.id)
            warehouse_root_locations.append(warehouse.view_location_id.id)
            warehouse_root_locations.append(warehouse.wh_pack_stock_loc_id.id)
            warehouse_root_locations.append(warehouse.wh_qc_stock_loc_id.id)
        warehouse_root_locations = filter(None, warehouse_root_locations)

        location = self.location_id
        while location.id not in warehouse_root_locations \
                and location.location_id:
            location = self.location_id.location_id

        if not location.parent_left or not location.parent_right:
            return

        self.env.cr.execute('''
            SELECT q.id FROM stock_quant q
            INNER JOIN stock_location l ON q.location_id = l.id
            WHERE q.product_id = %s
            AND l.parent_left >= %s
            AND l.parent_right <= %s
            AND l.usage = 'internal'
        ''', (self.product_id.id, location.parent_left, location.parent_right))

        result = [row[0] for row in self.env.cr.fetchall()]

        self.locations_with_product = result

    locations_with_product = fields.One2many(
        string='Internal Locations Of The Product',
        readonly=True,
        comodel_name='stock.quant',
        store=False,
        compute=_compute_locations_with_product
    )
