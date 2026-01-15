
# -*- coding: utf-8 -*-
from odoo import models, fields, api

class ItTicket(models.Model):
    _name = 'it.ticket'
    _description = 'IT Support Ticket'
    _rec_name = 'title'
    
    # Basic Fields
    title = fields.Char(string='Ticket Title', required=True, help='Tiêu đề sự cố')
    user_name = fields.Char(string='User Name', required=True, help='Tên người báo cáo')
    email = fields.Char(string='Email', required=True, help='Email liên hệ')
    description = fields.Text(string='Description', help='Mô tả chi tiết sự cố')
    priority = fields.Selection([
        ('low', 'Thấp'), 
        ('medium', 'Trung bình'), 
        ('high', 'Cao'), 
        ('critical', 'Khẩn cấp')
    ], string='Priority', default='medium', help='Mức độ ưu tiên của sự cố')
    category = fields.Selection([
        ('hardware', 'Phần cứng'), 
        ('software', 'Phần mềm'), 
        ('network', 'Mạng')
    ], string='Category', default='hardware', help='Loại sự cố')
    date_created = fields.Date(string='Date Created', default=fields.Date.context_today, help='Ngày báo cáo')
    deadline = fields.Date(string='Deadline', help='Hạn xử lý sự cố')
    is_resolved = fields.Boolean(string='Is Resolved', default=False, help='Đã được giải quyết chưa')

    tech_note = fields.Text(
        string='Technical Note', 
        help='Ghi chú kỹ thuật của nhân viên hỗ trợ',
        groups='it_support_ticket.group_it_technician'
    )
    
    repair_cost = fields.Integer(
        string='Repair Cost', 
        help='Chi phí sửa chữa (nếu có)',
        groups='it_support_ticket.group_it_manager'
    )
