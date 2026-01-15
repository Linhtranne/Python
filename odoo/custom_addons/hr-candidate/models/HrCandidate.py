# -*- coding: utf-8 -*-

from odoo import models, fields


class HrCandidate(models.Model):
    _name = 'hr.candidate'
    _description = 'Danh sách ứng viên tuyển dụng'

    name = fields.Char(string='Tên ứng viên', required=True)
    gender = fields.Selection(
        string='Giới tính',
        selection=[
            ('male', 'Name'), ('female', 'Nữ')
        ],
        help="Giới tính của ứng viên"
    )
    birthday = fields.Date(string='Ngày sinh')
    cv_content = fields.Text(string='Nội dung CV')
    expected_salary = fields.Integer(string='Mức lương mong muốn')
    is_hired = fields.Boolean(string='Đã tuyển?', default=False)
    manager_note = fields.Text(string='Ghi chú tuyển dụng')
    job_id = fields.Many2one(
        comodel_name='hr.job.position', 
        string='Vị trí ứng tuyển')
    offer_ids = fields.One2many(
        comodel_name='hr.candidate.offer', # Trỏ đến bảng con
        inverse_name='candidate_id',       # Tên cái cầu nối ở bảng con
        string='Lịch sử Offer'
    )
    tag_ids = fields.Many2many(
        comodel_name='hr.candidate.tag', 
        string='Kỹ năng (Tags)'
    )