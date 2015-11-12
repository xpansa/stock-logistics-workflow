# -*- coding: utf-8 -*-
# © 2015 Xpansa Group
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from openerp import api, fields, models


class StockMove(models.Model):
    _inherit = 'stock.move'

    @api.one
    @api.depends('product_id')
    def _compute_locations_with_product(self):
        if not self.product_id:
            return

        self.env.cr.execute('''
            SELECT q.id FROM stock_quant q
            INNER JOIN stock_location l ON q.location_id = l.id
            WHERE q.product_id = %s
            AND l.usage = 'internal'
        ''', (self.product_id.id,))

        result = [row[0] for row in self.env.cr.fetchall()]

        self.locations_with_product = result

    locations_with_product = fields.One2many(
        string='Internal Locations Of The Product',
        readonly=True,
        comodel_name='stock.quant',
        store=False,
        compute=_compute_locations_with_product
    )
