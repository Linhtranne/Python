# -*- coding: utf-8 -*-

from odoo import models, fields


class Student(models.Model):
    _name = 'student.management'
    _description = 'Student Management'

    name = fields.Char(string='Name', required=True)
    age = fields.Integer(string='Age')
    email = fields.Char(string='Email')
    is_active = fields.Boolean(string='Active', default=True)

