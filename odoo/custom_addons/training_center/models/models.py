# -*- coding: utf-8 -*-

from odoo import models, fields, api
from odoo.exceptions import ValidationError

# 1. MODEL MÔN HỌC
class TrainingSubject(models.Model):
    _name = 'training.subject'
    _description = 'Môn học'

    name = fields.Char(string="Tên môn", required=True)
    code = fields.Char(string="Mã môn")
    description = fields.Text(string="Mô tả đề cương")


# 2. MODEL GIẢNG VIÊN
class TrainingTeacher(models.Model):
    _name = 'training.teacher'
    _description = 'Giảng viên'

    name = fields.Char(string="Tên giảng viên", required=True)
    phone = fields.Char(string="Số điện thoại")
    skills = fields.Text(string="Kỹ năng")

# 3. MODEL SINH VIÊN
class TrainingStudent(models.Model):
    _name = 'training.student'
    _description = 'Sinh viên'

    name = fields.Char(string="Tên sinh viên", required=True)
    email = fields.Char(string="Email")
    student_id = fields.Char(string="Mã sinh viên")

# 4. MODEL LỚP HỌC
class TrainingClass(models.Model):
    _name = 'training.class'
    _description = 'Lớp học'

    name = fields.Char(string="Tên lớp")
    start_date = fields.Date(string="Ngày bắt đầu")
    end_date = fields.Date(string="Ngày kết thúc")
    duration = fields.Integer(string="Thời lượng (ngày)")
    _description = fields.Text(string="Mô tả lớp học")
    state = fields.Selection([
        ('draft', 'Dự thảo'),
        ('open', 'Đang mở'),
        ('closed', 'Đã đóng')
    ], string="Trạng thái", default='draft')
    price_per_student = fields.Integer(string="Học phí mỗi sinh viên",default = 1000000)
    total_revenue = fields.Integer(string="Tổng doanh thu", compute='_compute_total_revenue')
    @api.depends('student_ids', 'price_per_student')
    def _compute_total_revenue(self):
        for record in self:
            record.total_revenue = len(record.student_ids) * record.price_per_student
    @api.onchange('name', 'start_date')
    def _onchange_name_start_date(self):
        for record in self:
            if record.name and record.start_date:
                record._description = f"Lớp {record.name} bắt đầu từ {record.start_date} thì ngon luôn"
    @api.onchange('price_per_student')
    def _onchange_price(self):
            if self.price_per_student < 1000000:
                return {
                    'warning': {
                        'title': "ĐÓNG NHIỀU LÊN",
                        'message': "NGU.",
                    }
                }
    @api.constrains('name')
    def _constrains_name(self):
        for record in self:
                if not record.name or not record.name.strip():
                    raise ValidationError("Hehe","Tên lớp không được bỏ trống")
                elif  len(record.name.strip()) < 20 or len(record.name.strip()) >8:
                    raise ValidationError("Ngu.")
    state = fields.Selection([
        ('draft', 'Dự thảo'),
        ('open', 'Đang mở'),
        ('closed', 'Đã đóng')], string="Trạng thái", default='draft')
    def action_open(self):
        for record in self:
            if not record.start_date:
                raise ValidationError("Vui lòng nhập Ngày bắt đầu trước khi mở lớp.")
            record.state = 'open'
    def action_close(self):
        for record in self:
            record.state = 'closed'
    def action_draft(self):
        for record in self:
            record.state = 'draft'
    subject_id = fields.Many2one('training.subject', string="Môn học", required=True)
    teacher_id = fields.Many2one('training.teacher', string="Giảng viên")
    student_ids = fields.Many2many('training.student', string="Danh sách sinh viên")
    session_ids = fields.One2many('training.session', 'class_id', string="Lịch học chi tiết")
    _sql_constraints = [
        ('duration_positive', 'CHECK(duration > 3)', 'Thời lượng phải lớn hơn 3')
    ]
    

# 5. MODEL BUỔI HỌC (SESSION)
class TrainingSession(models.Model):
    _name = 'training.session'
    _description = 'Buổi học'

    name = fields.Char(string="Nội dung buổi học", required=True)
    date = fields.Date(string="Ngày học", default=fields.Date.today)
    duration = fields.Integer(string="Thời lượng (phút)")
    
    # Many2one ngược về Lớp học
    class_id = fields.Many2one('training.class', string="Lớp học")