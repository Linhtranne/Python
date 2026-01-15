# -*- coding: utf-8 -*-

from odoo import models, fields


class InventoryProduct(models.Model):
    _name = 'inventory.product'
    _description = 'Inventory Product'
    _rec_name = 'name'

    name = fields.Char(string='Product Name', required=True, help='Name of the product')
    price = fields.Float(string='Price', help='Product price')
    stock = fields.Integer(string='Stock', help='Quantity in stock')
