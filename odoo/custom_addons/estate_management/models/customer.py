# -*- coding: utf-8 -*-

from odoo import models, fields, api


class Customer(models.Model):
    _name = 'estate.customer'
    _description = 'Customer Management'
    _rec_name = 'name'

    name = fields.Char(string='Customer Name', required=True, help='Full name of the customer')
    email = fields.Char(string='Email', help='Customer email address')
    phone = fields.Char(string='Phone', help='Customer phone number')
    address = fields.Text(string='Address', help='Customer address')
    
    # One2many relationship: One customer can have many properties
    property_ids = fields.One2many(
        'estate.property',
        'customer_id',
        string='Properties',
        help='List of properties owned by this customer'
    )
    
    # Computed field: Count total properties
    property_count = fields.Integer(
        string='Property Count',
        compute='_compute_property_count',
        help='Total number of properties owned by this customer'
    )
    
    @api.depends('property_ids')
    def _compute_property_count(self):
        for record in self:
            record.property_count = len(record.property_ids)
    
    def action_view_properties(self):
        """Action to view all properties of this customer"""
        return {
            'name': 'Properties',
            'type': 'ir.actions.act_window',
            'res_model': 'estate.property',
            'view_mode': 'tree,form',
            'domain': [('customer_id', '=', self.id)],
            'context': {'default_customer_id': self.id},
        }
