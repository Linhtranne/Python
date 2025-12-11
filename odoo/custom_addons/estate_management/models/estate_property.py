# -*- coding: utf-8 -*-

from odoo import models, fields


class EstateProperty(models.Model):
    _name = 'estate.property'
    _description = 'Estate Property Management'
    _rec_name = 'name'

    name = fields.Char(string='Property Name', required=True, help='Name or identifier of the property')
    address = fields.Text(string='Address', required=True, help='Property address')
    property_type = fields.Selection([
        ('house', 'House'),
        ('apartment', 'Apartment'),
        ('villa', 'Villa'),
        ('land', 'Land'),
        ('commercial', 'Commercial'),
    ], string='Property Type', default='house', help='Type of the property')
    
    area = fields.Float(string='Area (m²)', help='Total area in square meters')
    bedrooms = fields.Integer(string='Bedrooms', help='Number of bedrooms')
    bathrooms = fields.Integer(string='Bathrooms', help='Number of bathrooms')
    price = fields.Float(string='Price', help='Property price')
    
    # Many2one relationship: Each property belongs to one customer
    customer_id = fields.Many2one(
        'estate.customer',
        string='Owner',
        required=True,
        ondelete='cascade',
        help='Customer who owns this property'
    )
    
    status = fields.Selection([
        ('available', 'Available'),
        ('sold', 'Sold'),
        ('rented', 'Rented'),
    ], string='Status', default='available', help='Current status of the property')
    
    description = fields.Text(string='Description', help='Additional property details')
