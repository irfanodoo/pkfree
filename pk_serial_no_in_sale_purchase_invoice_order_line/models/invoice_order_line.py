# -*- coding: utf-8 -*-

from odoo import api, fields, models


class AccountMove(models.Model):
    _inherit = 'account.move'

    @api.onchange('invoice_line_ids')
    def _onchange_order_line_set_sn(self):
        sl_no = 1
        for line in self.invoice_line_ids:
            if line.display_type not in ['line_note', 'line_section']:
                line.sl_no = sl_no
                sl_no += 1
            else:
                line.sl_no = False


class AccountMoveLine(models.Model):
    _inherit = 'account.move.line'

    sl_no = fields.Integer(string='Sl. No.', store="1", copy=False)
    # def _prepare_invoice_line(self):
    #     res = super(AccountMoveLine, self)._prepare_invoice_line()
    #     res['sl_no'] = self.sl_no
    #     return res
