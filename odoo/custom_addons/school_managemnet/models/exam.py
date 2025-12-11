# -*- coding: utf-8 -*-

from odoo import models, fields, api


class Exam(models.Model):
    _name = 'exam.management'
    _description = 'Exam Management'
    _rec_name = 'subject'

    exam_date = fields.Date(string='Exam Date', required=True, help='Date of the exam')
    subject = fields.Char(string='Subject', required=True, help='Subject name')
    school_id = fields.Many2one('school.management', string='School', required=True, help='School conducting the exam')
    
    # Many2many relationship with students
    students = fields.Many2many('student.management', 'student_exam_rel', 'exam_id', 'student_id', string='Students')
    
    score = fields.Float(string='Score', help='Exam score')
    
    # Computed fields
    student_count = fields.Integer(string='Total Students', compute='_compute_student_count')
    average_exam_score = fields.Float(string='Exam Average', compute='_compute_average_exam_score')

    @api.depends('students')
    def _compute_student_count(self):
        for record in self:
            record.student_count = len(record.students)

    @api.depends('students', 'students.score')
    def _compute_average_exam_score(self):
        """Calculate average score of all students in this exam"""
        for record in self:
            if record.students:
                total_score = sum(student.score for student in record.students if student.score)
                record.average_exam_score = total_score / len(record.students) if record.students else 0.0
            else:
                record.average_exam_score = 0.0

    def action_view_students(self):
        """View all students in this exam"""
        return {
            'type': 'ir.actions.act_window',
            'name': 'Exam Students',
            'res_model': 'student.management',
            'view_mode': 'tree,form',
            'domain': [('id', 'in', self.students.ids)],
        }

    def action_calculate_exam_average(self):
        """Calculate and display exam average"""
        for record in self:
            if record.students:
                total_score = sum(student.score for student in record.students if student.score)
                avg = total_score / len(record.students) if record.students else 0.0
                record.average_exam_score = avg
        
        return {
            'type': 'ir.actions.client',
            'tag': 'display_notification',
            'params': {
                'title': 'Exam Average',
                'message': f'Average score: {self.average_exam_score:.2f}',
                'type': 'info',
                'sticky': False,
            }
        }
