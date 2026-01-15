# -*- coding: utf-8 -*-

from odoo import models, fields


class SchoolStudent(models.Model):
    _name = 'school.student'
    _description = 'School Student'
    _rec_name = 'name'

    name = fields.Char(string='Student Name', required=True, help='Full name of the student')
    age = fields.Integer(string='Age', help='Student age')
    bio = fields.Text(string='Biography', help='Student biography and additional information')
    is_active = fields.Boolean(string='Active', default=True, help='Set to False to archive the student')
