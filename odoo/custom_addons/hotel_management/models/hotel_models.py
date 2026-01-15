# -*- coding: utf-8 -*-
from odoo import models, fields, api
from odoo.exceptions import ValidationError

class HotelRoom(models.Model):
    _name = 'hotel.room'
    _description = 'Phòng khách sạn'

    name = fields.Char(string='Tên phòng', required=True)
    status = fields.Selection([
        ('available', 'Trống'),
        ('occupied', 'Đang ở'),
        ('maintenance', 'Bảo trì'),
    ], string='Trạng thái', default='available')

class HotelBooking(models.Model):
    _name = 'hotel.booking'
    _description = 'Đặt phòng khách sạn'

    name = fields.Char(string='Mã đặt phòng', required=True, default=lambda self: 'New')
    student_id = fields.Many2one('res.partner', string='Khách/Sinh viên', required=True)
    room_id = fields.Many2one('hotel.room', string='Phòng', required=True)
    checkin_date = fields.Date(string='Ngày nhận phòng', required=True)
    checkout_date = fields.Date(string='Ngày trả phòng', required=True)
    state = fields.Selection([
        ('draft', 'Nháp'),
        ('confirmed', 'Đã xác nhận'),
        ('done', 'Hoàn thành'),
        ('cancel', 'Đã hủy')
    ], string='Trạng thái', default='draft', tracking=True)

    # BUTTON LOGIC
    def action_confirm(self):
        for rec in self:
            if rec.state != 'draft':
                continue
            if rec.room_id.status in ['maintenance', 'occupied']:
                raise ValidationError('Phòng đang bảo trì hoặc đã có người ở!')
            rec.state = 'confirmed'
            rec.room_id.status = 'occupied'

    def action_done(self):
        for rec in self:
            if rec.state != 'confirmed':
                continue
            rec.state = 'done'
            rec.room_id.status = 'available'

    def action_cancel(self):
        for rec in self:
            if rec.state not in ['draft', 'confirmed']:
                continue
            rec.state = 'cancel'
            if rec.state == 'confirmed':
                rec.room_id.status = 'available'

    def action_draft(self):
        for rec in self:
            rec.state = 'draft'
