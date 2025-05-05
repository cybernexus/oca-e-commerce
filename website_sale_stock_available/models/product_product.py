# Copyright 2020 Tecnativa - Ernesto Tejeda
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo import models


class Product(models.Model):
    _inherit = "product.product"

    def _compute_available_quantities_dict(self):
        res = super()._compute_available_quantities_dict()

        if self.env.context.get("website_sale_stock_available"):
            for product in self.with_context(website_sale_stock_available=False):
                immediately = product.immediately_usable_qty
                product.free_qty = immediately
                res[product.id]["free_qty"] = immediately
