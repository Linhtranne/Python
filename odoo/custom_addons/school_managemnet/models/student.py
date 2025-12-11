# -*- coding: utf-8 -*-

from odoo import models, fields, api


class Student(models.Model):
    _name = 'student.management'
    _description = 'Student Management'
    _rec_name = 'name'

    name = fields.Char(string='Student Name', required=True, help='Full name of the student')
    age = fields.Integer(string='Age', help='Age of the student')
    school_id = fields.Many2one('school.management', string='School', required=True, help='School the student belongs to')
    score = fields.Float(string='Score', help='Student exam score')
    
    # Many2many relationship with exams
    exam_ids = fields.Many2many('exam.management', 'student_exam_rel', 'student_id', 'exam_id', string='Exams')
    
    # Computed field
    exam_count = fields.Integer(string='Total Exams', compute='_compute_exam_count')
    average_score = fields.Float(string='Average Score', compute='_compute_average_score', store=True)

    @api.depends('exam_ids')
    def _compute_exam_count(self):
        for record in self:
            record.exam_count = len(record.exam_ids)

    @api.depends('exam_ids', 'exam_ids.score')
    def _compute_average_score(self):
        """Calculate average score from all exams"""
        for record in self:
            if record.exam_ids:
                total_score = sum(exam.score for exam in record.exam_ids if exam.score)
                record.average_score = total_score / len(record.exam_ids) if record.exam_ids else 0.0
            else:
                record.average_score = 0.0

    # CRUD Methods
    def action_update_student(self):
        """Method to update student information"""
        return {
            'type': 'ir.actions.act_window',
            'name': 'Update Student',
            'res_model': 'student.management',
            'view_mode': 'form',
            'res_id': self.id,
            'target': 'current',
        }

    def action_calculate_average(self):
        """Calculate and update average score"""
        for record in self:
            if record.exam_ids:
                total_score = sum(exam.score for exam in record.exam_ids if exam.score)
                record.average_score = total_score / len(record.exam_ids) if record.exam_ids else 0.0
            else:
                record.average_score = 0.0
        
        return {
            'type': 'ir.actions.client',
            'tag': 'display_notification',
            'params': {
                'title': 'Success',
                'message': 'Average score calculated successfully!',
                'type': 'success',
                'sticky': False,
            }
        }

    def action_view_exams(self):
        """View all exams of this student"""
        return {
            'type': 'ir.actions.act_window',
            'name': 'Student Exams',
            'res_model': 'exam.management',
            'view_mode': 'tree,form',
            'domain': [('students', 'in', [self.id])],
        }
