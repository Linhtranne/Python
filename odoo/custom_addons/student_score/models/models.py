# -*- coding: utf-8 -*-

# from odoo import models, fields, api


# class student_score(models.Model):
#     _name = 'student_score.student_score'
#     _description = 'student_score.student_score'

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100

