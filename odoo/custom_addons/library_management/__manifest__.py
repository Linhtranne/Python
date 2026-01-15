# -*- coding: utf-8 -*-
{
    'name': 'Library Management',
    'version': '1.0',
    'category': 'Education',
    'summary': 'Quản lý thư viện trường học',
    'description': """
        Module quản lý thư viện
    """,
    'author': 'Your Name',
    'website': 'https://www.example.com',
    'depends': ['base'],
    'data': [
        'security/library_groups.xml',
        'security/ir.model.access.csv',
        'views/library_menus.xml',
        'views/library_views.xml',
        'demo/library_demo.xml',
    ],
    'installable': True,
    'application': True,
    'auto_install': False,
    'license': 'LGPL-3',
}