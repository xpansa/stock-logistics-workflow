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

        quants = self.env['stock.quant'].search([
            ('product_id', '=', self.product_id.id),
            ('location_id.usage', '=', 'internal')
        ])

        self.locations_with_product = quants

    locations_with_product = fields.One2many(
        string='Internal Locations Of The Product',
        readonly=True,
        comodel_name='stock.quant',
        store=False,
        compute=_compute_locations_with_product
    )
