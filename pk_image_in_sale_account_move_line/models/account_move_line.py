from odoo import models, fields, api


class InvoiceOrderLine(models.Model):
    _inherit = 'account.move.line'

    order_line_image = fields.Binary(string="Image")
