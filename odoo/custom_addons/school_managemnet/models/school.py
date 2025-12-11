# -*- coding: utf-8 -*-

from odoo import models, fields, api


class School(models.Model):
    _name = 'school.management'
    _description = 'School Management'
    _rec_name = 'name'

    name = fields.Char(string='School Name', required=True, help='Name of the school')
    location = fields.Char(string='Location', help='School address')
    start_date = fields.Date(string='Start Date', help='School establishment date')
    
    # One2many relationship
    student_ids = fields.One2many('student.management', 'school_id', string='Students')
    exam_ids = fields.One2many('exam.management', 'school_id', string='Exams')
    
    # Computed fields
    student_count = fields.Integer(string='Total Students', compute='_compute_student_count')
    exam_count = fields.Integer(string='Total Exams', compute='_compute_exam_count')

    @api.depends('student_ids')
    def _compute_student_count(self):
        for record in self:
            record.student_count = len(record.student_ids)

    @api.depends('exam_ids')
    def _compute_exam_count(self):
        for record in self:
            record.exam_count = len(record.exam_ids)

    # CRUD Methods
    def action_update_school(self):
        """Method to update school information"""
        return {
            'type': 'ir.actions.act_window',
            'name': 'Update School',
            'res_model': 'school.management',
            'view_mode': 'form',
            'res_id': self.id,
            'target': 'current',
        }

    def action_view_students(self):
        """View all students in this school"""
        return {
            'type': 'ir.actions.act_window',
            'name': 'Students',
            'res_model': 'student.management',
            'view_mode': 'tree,form',
            'domain': [('school_id', '=', self.id)],
            'context': {'default_school_id': self.id},
        }

    def action_view_exams(self):
        """View all exams in this school"""
        return {
            'type': 'ir.actions.act_window',
            'name': 'Exams',
            'res_model': 'exam.management',
            'view_mode': 'tree,form',
            'domain': [('school_id', '=', self.id)],
            'context': {'default_school_id': self.id},
        }
