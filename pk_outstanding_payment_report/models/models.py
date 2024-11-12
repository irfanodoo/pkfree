from odoo import models, fields

class ResPartner(models.Model):
    _inherit = 'res.partner'

    unpaid_invoices = fields.One2many(
        comodel_name='account.move',
        compute='_compute_unpaid_invoices',
        string='Outstanding Invoices',
    )

    def _compute_unpaid_invoices(self):
        for partner in self:
            partner.unpaid_invoices = self.env['account.move'].search([
                ('partner_id', '=', partner.id),
                ('state', '=', 'posted'),
                ('payment_state', '!=', 'paid'),
                ('move_type', '=', 'out_invoice')
            ])


