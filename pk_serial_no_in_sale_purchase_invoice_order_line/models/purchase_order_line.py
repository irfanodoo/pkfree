# -*- coding: utf-8 -*-##
from odoo import api, fields, models


class PurchaseOrder(models.Model):
    _inherit = 'purchase.order'

    @api.onchange('order_line')
    def _onchange_order_line_set_sn(self):
        sl_no = 1
        for line in self.order_line:
            if line.display_type not in ['line_note', 'line_section']:
                line.sl_no = sl_no
                sl_no += 1
            else:
                line.sl_no = False


class PurchaseOrderLine(models.Model):
    _inherit = 'purchase.order.line'

    sl_no = fields.Integer(string='Sl. No.', store=True, copy=False)

    def _prepare_account_move_line(self):
        res = super(PurchaseOrderLine, self)._prepare_account_move_line()
        res['sl_no'] = self.sl_no
        return res
