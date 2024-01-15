from odoo import models, fields


class SaleOrderLine(models.Model):
    _inherit = 'sale.order.line'

    sl_no = fields.Integer(string='Sl. No.', store="1", copy=False)

    def _prepare_invoice_line(self, **optional_values):
        res = super(SaleOrderLine, self)._prepare_invoice_line(**optional_values)
        res['sl_no'] = self.sl_no
        return res
