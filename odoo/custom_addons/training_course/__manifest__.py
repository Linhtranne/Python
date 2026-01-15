# -*- coding: utf-8 -*-
{
    'name': "Training Course",

    'summary': "Training Course Management System",

    'description': """
Training Course Management Module
- Manage training courses
- Track course duration and status
    """,

    'author': "Odoo Developer",
    'website': "https://www.odoo.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/15.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Education',
    'version': '17.0.1.0.0',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'views/course_views.xml',
        'views/student_views.xml',
        'views/product_views.xml',
        'views/menu_views.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
        'installable': True,
    'application': True,
    'license': 'LGPL-3',
}

