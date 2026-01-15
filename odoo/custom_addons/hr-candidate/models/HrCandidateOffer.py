#-*- coding: utf-8 -*-

from odoo import models, fields

class HrCandidateOffer(models.Model):
    _name = 'hr.candidate.offer'
    _description = 'Lịch sử mời làm việc'

    price = fields.Integer(string='Mức lương đề nghị')
    status = fields.Selection([
        ('accepted', 'Đồng ý'),
        ('refused', 'Từ chối')
    ], string='Trạng thái')
    candidate_id = fields.Many2one(
        comodel_name='hr.candidate', 
        string='Ứng viên', 
        required=True
    )