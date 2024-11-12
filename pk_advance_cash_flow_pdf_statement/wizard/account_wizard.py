import json
from datetime import datetime
import xlsxwriter

from odoo import models, fields, _
from odoo.exceptions import UserError
from odoo.tools import date_utils, io


class AccountWizardPDF(models.TransientModel):
    _name = "account.wizard"
    _description = 'Account Wizard'

    name = fields.Char(default="Invoice", help='Name of Invoice ')
    date_from = fields.Date(string="Start Date", require=True,
                            help='Date at which report need to be start')
    date_to = fields.Date(string="End Date", default=fields.Date.today,
                          help='Date at which report need to be end')
    today = fields.Date("Report Date", default=fields.Date.today,
                        help='Date at which report is generated')

    def print_pdf_report(self):
        """ Generate xlsx report return values to template"""
        date_from = datetime.strptime(str(self.date_from), "%Y-%m-%d")
        date_to = datetime.strptime(str(self.date_to), "%Y-%m-%d")
        if date_from:
            if date_from > date_to:
                raise UserError(_("Start date should be less than end date"))
        data = {
            'ids': self.ids,
            'model': self._name,
            'date_from': self.date_from,
            'date_to': self.date_to,
            # 'levels': self.levels,
            # 'target_move': self.target_move,
            'today': self.today,
        }
        return self.env.ref('pk_advance_cash_flow_pdf_statement.pdf_cash_flow_report_id').report_action(self, data=data)

 