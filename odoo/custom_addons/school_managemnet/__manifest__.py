# -*- coding: utf-8 -*-
{
    'name': "School Management",
    'summary': "Manage schools, students and exams",
    'description': """
        School Management Module
        =========================
        * Manage schools information
        * Manage students linked to schools
        * Manage exams and student scores
        * Calculate student average scores
    """,
    'author': "Your Company",
    'category': 'Education',
    'version': '1.0',
    'depends': ['base'],
    'data': [
        'security/ir.model.access.csv',
        'views/school_views.xml',
        'views/student_views.xml',
        'views/exam_views.xml',
        'views/menu_views.xml',
    ],
    'demo': [],
    'installable': True,
    'application': True,
    'license': 'LGPL-3',
}

