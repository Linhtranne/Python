# -*- coding: utf-8 -*-
{
    'name': "Student Management",
    'summary': "Manage students",
    'description': """Student Management Module""",
    'author': "Your Company",
    'category': 'Education',
    'version': '1.0',
    'depends': ['base'],
    'data': [
        'security/ir.model.access.csv',
        'views/student_views.xml',
        'views/student_menu.xml',
    ],
    'installable': True,
    'application': True,
    'license': 'LGPL-3',
}

