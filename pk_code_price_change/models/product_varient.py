from odoo import models, fields, api

class ProductProductPriceCode(models.Model):
    _inherit = 'product.product'

    price_code = fields.Char(
        string="Price Code",
        help="Products with the same price code will have synchronized prices."
    )

    def write(self, vals):
        # Prevent recursion by using a context flag
        if self.env.context.get('skip_price_sync'):
            return super(ProductProductPriceCode, self).write(vals)

        # Only proceed if `lst_price` is in vals and the product has a `price_code`
        if 'lst_price' in vals:
            for record in self:
                if record.price_code:
                    # Find other products with the same price_code
                    products_to_update = self.with_context(skip_price_sync=True).search([
                        ('price_code', '=', record.price_code) # Exclude the current product
                    ])
                    # Update the price for those products
                    products_to_update.write({'lst_price': vals['lst_price']})

        # Write the original values
        return super(ProductProductPriceCode, self).write(vals)
