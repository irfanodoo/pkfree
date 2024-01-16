from odoo import fields, models


class SaleOrderLine(models.Model):
    _inherit = 'sale.order.line'

    order_line_image = fields.Binary(string="Image")


class InvoiceOrderLine(models.Model):
    _inherit = 'account.move.line'

    order_line_image = fields.Binary(string="Image")
