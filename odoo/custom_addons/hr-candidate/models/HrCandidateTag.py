# -*- coding: utf-8 -*-
from odoo import models, fields
class HrCandidateTag(models.Model):
    _name = 'hr.candidate.tag'
    _description = 'Kỹ năng ứng viên'

    name = fields.Char(string='Tên kỹ năng', required=True)
    color = fields.Integer(string='Màu sắc') # Để hiển thị màu trên giao diện