# -*- coding: utf-8 -*-

from odoo import models, fields, api


class ReportInvoice(models.AbstractModel):
    _inherit = 'account.move'

    def _get_grouped_invoice_lines(self):
        """Group invoice lines by product and sum quantities, prices, and show tax rate"""
        line_data = {}

        for line in self.invoice_line_ids:
            product = line.product_id
            total_price = line.price_unit * line.quantity  # Calculate total price (unit price * quantity)

            # Get the tax rate for the product (assuming all taxes are the same)
            tax_rate = 0
            if line.tax_ids:
                tax_rate = line.tax_ids[0].amount  # Take the first tax rate (as it's applied globally for this line)

            if product.id not in line_data:
                line_data[product.id] = {
                    'product_name': product.display_name,
                    'total_quantity': line.quantity,
                    'unit_price': line.price_unit,  # Add unit price
                    'total_price': total_price,  # Total price for the product
                    'tax_rate': tax_rate,  # Store the tax rate
                    # 'total_amount': total_price + (total_price * tax_rate / 100)  # Calculate the total amount including tax
                }
            else:
                # Group by product and sum values
                line_data[product.id]['total_quantity'] += line.quantity
                line_data[product.id]['total_price'] += total_price
                # line_data[product.id]['total_amount'] += (total_price + (total_price * tax_rate / 100))

        return list(line_data.values())

