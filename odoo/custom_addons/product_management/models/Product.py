
from odoo import models, fields
class Product(models.Model):
    _name = 'product.management'
    _description = 'Product Management'

    product_name = fields.Char(string='Product Name', required=True)
    product_price = fields.Float(string='Product Price', required=True)
    product_quantity = fields.Integer(string='Product Quantity', default=0)
