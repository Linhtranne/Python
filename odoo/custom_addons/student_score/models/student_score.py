# -*- coding: utf-8 -*-

from odoo import models, fields, api


class StudentScore(models.Model):
    _inherit = 'student.management'

    score_math = fields.Float(string='Math Score')
    score_english = fields.Float(string='English Score')
    score_average = fields.Float(string='Average Score', compute='_compute_score_average', store=True)

    @api.depends('score_math', 'score_english')
    def _compute_score_average(self):
        for record in self:
            if record.score_math or record.score_english:
                total = (record.score_math or 0) + (record.score_english or 0)
                record.score_average = total / 2
            else:
                record.score_average = 0

    def action_calculate_average(self):
        for record in self:
            if record.score_math or record.score_english:
                total = (record.score_math or 0) + (record.score_english or 0)
                record.score_average = total / 2
            else:
                record.score_average = 0
