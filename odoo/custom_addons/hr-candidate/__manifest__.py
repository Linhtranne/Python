# -*- coding: utf-8 -*-
{
    'name': "recruitment",

    'summary': "Short (1 phrase/line) summary of the module's purpose",

    'description': """
Long description of module's purpose
    """,

    'author': "My Company",
    'website': "https://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check odoo/odoo/addons/base/data/ir_module_category_data.xml at 15.0 · odoo/odoo
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        'security/hr_security.xml',
        'security/ir.model.access.csv',
        'security/hr_rules.xml',
        'views/views.xml',
        'views/menu.xml',

    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
    'application': True,
    'installable': True,
    'license': 'LGPL-3'
}