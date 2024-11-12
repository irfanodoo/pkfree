from odoo import models, fields, api

class ProductTemplate(models.Model):
    _inherit = 'product.template'

    code = fields.Char(string="Price Code", help="Products with the same code will have synchronized prices.")

    @api.model
    def write(self, vals):
        # Check if we are in a recursive call to avoid infinite recursion
        if self.env.context.get('skip_price_sync'):
            return super().write(vals)

        # Loop through the records
        for record in self:
            if 'list_price' in vals:
                # Find other products with the same code
                products_to_update = self.with_context(skip_price_sync=True).search([('code', '=', record.code)])
                # Update the price for those products
                products_to_update.write({'list_price': vals['list_price']})

        # Call the super write method for the main operation
        return super().write(vals)

    # @api.model
    # def create(self, vals):
    #     # Ensure code is unique across products, if required
    #     if 'code' in vals and vals['code']:
    #         existing_product = self.search([('code', '=', vals['code'])], limit=1)
    #         if existing_product:
    #             raise ValueError("Code must be unique across products.")
    #     return super(ProductTemplate, self).create(vals)

