# -*- coding: utf-8 -*-

from odoo import models, fields


class TrainingCourse(models.Model):
    _name = 'training.course'
    _description = 'Training Course'
    _rec_name = 'name'

    name = fields.Char(string='Course Name', required=True, help='Name of the training course')
    duration = fields.Integer(string='Duration (hours)', help='Course duration in hours')
    active = fields.Boolean(string='Active', default=True, help='Set to False to archive the course')
