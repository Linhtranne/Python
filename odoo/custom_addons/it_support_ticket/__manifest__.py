# -*- coding: utf-8 -*-
{
    'name': "IT Support Ticket",
    'description': """
        IT Support Ticket Module
        - Manage IT support tickets
        - Track ticket status and priority
        - Assign tickets to support agents
    """,
    'author': "Odoo Developer",
    'website': "https://www.odoo.com",
    'category': 'Services',
    'version': '17.0.1.0.0',
    'depends': ['base'],
    'data': [
        'security/it_groups.xml',
        'security/ir.model.access.csv',
        'security/it_rules.xml',
    ],
    'installable': True,
    'application': True,
    'auto_install': False,
    'license': 'LGPL-3',
}

