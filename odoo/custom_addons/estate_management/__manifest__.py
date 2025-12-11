# -*- coding: utf-8 -*-
{
    'name': "Estate Management",
    'summary': """Customer and Property Management System""",
    'description': """
        Estate Management Module
        - Manage Customers and their Properties
        - Track Revenue
        - Calculate total revenue by date
    """,
    'author': "Odoo Developer",
    'website': "https://www.odoo.com",
    'category': 'Real Estate',
    'version': '17.0.1.0.0',
    'depends': ['base'],
    'data': [
        'security/ir.model.access.csv',
        'views/customer_views.xml',
        'views/estate_property_views.xml',
        'views/revenue_views.xml',
        'views/menu_views.xml',
    ],
    'installable': True,
    'application': True,
    'auto_install': False,
}
