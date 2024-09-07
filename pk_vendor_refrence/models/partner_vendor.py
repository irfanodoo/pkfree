# -*- coding: utf-8 -*-

from odoo import models, fields


class VendorRef(models.Model):
    _inherit = 'product.supplierinfo'

    vendor_ref = fields.Char(related="partner_id.ref", string="Vendor Reference")

