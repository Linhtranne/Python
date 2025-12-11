# -*- coding: utf-8 -*-
{
    'name': "Bookstore Management",
    'summary': "Manage bookstore and books",
    'description': """
        Bookstore Management Module
        - Manage books information
        - Track title, author, price, publish date
    """,
    'author': "Your Company",
    'category': 'Sales',
    'version': '1.0',
    'depends': ['base'],
    'data': [
        'security/ir.model.access.csv',
        'views/book_views.xml',
        'views/menu_views.xml',
    ],
    'demo': [],
    'installable': True,
    'application': True,
    'license': 'LGPL-3',
}

