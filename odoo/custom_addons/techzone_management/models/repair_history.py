# -*- coding: utf-8 -*-

from odoo import models, fields, api


class RepairHistory(models.Model):
    _name = 'repair.history'
    _description = 'Lịch sử sự cố'
    _order = 'date_log desc'

    device_id = fields.Many2one(
        comodel_name='repair.device',
        string='Thiết bị',
        required=True,
        ondelete='cascade'
    )
    
    order_id = fields.Many2one(
        comodel_name='repair.order',
        string='Phiếu sửa chữa',
        help='Link tới phiếu sửa chữa nếu có'
    )
    
    issue_description = fields.Text(
        string='Mô tả lỗi',
        required=True,
        help='Mô tả chi tiết về lỗi của thiết bị'
    )
    
    diagnosis_result = fields.Text(
        string='Kết quả kiểm tra',
        help='Kết quả kiểm tra và chẩn đoán lỗi'
    )
    
    date_log = fields.Date(
        string='Ngày ghi nhận',
        required=True,
        default=fields.Date.today
    )
    
    technician_id = fields.Many2one(
        comodel_name='res.users',
        string='Kỹ thuật viên',
        default=lambda self: self.env.user
    )
    
    image_ids = fields.Many2many(
        comodel_name='ir.attachment',
        string='Hình ảnh lỗi',
        help='Hình ảnh mô tả lỗi của thiết bị'
    )


class RepairDiagnosis(models.Model):
    _name = 'repair.diagnosis'
    _description = 'Danh sách kiểm tra (Checklist)'

    name = fields.Char(
        string='Hạng mục kiểm tra',
        required=True,
        help='Tên hạng mục cần kiểm tra (Loa, Mic, Màn hình, Cảm ứng...)'
    )
    
    description = fields.Text(
        string='Mô tả',
        help='Mô tả chi tiết về hạng mục kiểm tra'
    )
    
    is_active = fields.Boolean(
        string='Đang sử dụng',
        default=True
    )
