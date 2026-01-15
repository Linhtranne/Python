# -*- coding: utf-8 -*-
{
    'name': "finance_expense",
    'description': """
        Estate Management Module
        - Manage Customers and their Properties
        - Track Revenue
        - Calculate total revenue by date
    """,
    'author': "Odoo Developer",
    'website': "https://www.odoo.com",
    'category': 'Finance',
    'version': '17.0.1.0.0',
    'depends': ['base'],
    'data': [
        'security/finance_groups.xml',
        'security/ir.model.access.csv',
        'security/finance_rules.xml'
    ],
    'installable': True,
    'application': True,
    'auto_install': False,
    'lisense': 'LGPL-3',
}

