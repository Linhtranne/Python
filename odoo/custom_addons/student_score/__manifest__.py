# -*- coding: utf-8 -*-
{
    'name': "Student Score",
    'summary': "Add score fields to student management",
    'description': """
        Student Score Module
        - Add math and english scores
        - Calculate average score
    """,
    'author': "Your Company",
    'category': 'Education',
    'version': '1.0',
    'depends': ['student_management'],
    'data': [
        'views/student_score_views.xml',
    ],
    'installable': True,
    'application': False,
    'license': 'LGPL-3',
}


