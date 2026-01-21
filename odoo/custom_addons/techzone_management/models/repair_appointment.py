# -*- coding: utf-8 -*-

from odoo import models, fields, api, _


class RepairAppointment(models.Model):
    _name = 'repair.appointment'
    _description = 'Lịch hẹn sửa chữa'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _order = 'appointment_date desc'

    name = fields.Char(
        string='Mã lịch hẹn',
        required=True,
        readonly=True,
        copy=False,
        default='New',
        help='Mã lịch hẹn tự động'
    )
    
    partner_id = fields.Many2one(
        comodel_name='res.partner',
        string='Khách hàng',
        required=True,
        tracking=True
    )
    
    device_id = fields.Many2one(
        comodel_name='repair.device',
        string='Thiết bị',
        domain="[('owner_id', '=', partner_id)]"
    )
    
    appointment_date = fields.Datetime(
        string='Ngày giờ hẹn',
        required=True,
        tracking=True,
        help='Ngày giờ khách hẹn mang máy đến'
    )
    
    note = fields.Text(
        string='Mô tả lỗi sơ bộ',
        help='Mô tả sơ bộ về lỗi của thiết bị'
    )
    
    state = fields.Selection(
        string='Trạng thái',
        selection=[
            ('scheduled', 'Đã hẹn'),
            ('confirmed', 'Đã xác nhận'),
            ('completed', 'Đã hoàn thành'),
            ('cancelled', 'Đã hủy'),
        ],
        default='scheduled',
        tracking=True
    )

    @api.model
    def create(self, vals):
        """Tạo mã lịch hẹn tự động"""
        if vals.get('name', 'New') == 'New':
            vals['name'] = self.env['ir.sequence'].next_by_code('repair.appointment') or 'New'
        return super().create(vals)
