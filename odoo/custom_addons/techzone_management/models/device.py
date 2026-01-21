# -*- coding: utf-8 -*-

from odoo import models, fields, api
from odoo.exceptions import ValidationError


class RepairDevice(models.Model):
    _name = 'repair.device'
    _description = 'Thiết bị sửa chữa'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _order = 'name'

    name = fields.Char(
        string='Mã thiết bị',
        required=True,
        copy=False,
        readonly=True,
        default='New'
    )
    
    serial_number = fields.Char(
        string='IMEI/Serial',
        required=True,
        help='IMEI hoặc số serial của thiết bị (duy nhất)'
    )
    
    image = fields.Binary(
        string='Hình ảnh',
        attachment=True
    )
    
    model_name = fields.Char(
        string='Tên Model',
        help='Tên model của thiết bị'
    )
    
    purchase_date = fields.Date(
        string='Ngày mua',
        help='Ngày mua thiết bị'
    )
    
    warranty_status = fields.Selection(
        string='Trạng thái bảo hành',
        selection=[
            ('warranty', 'Còn bảo hành'),
            ('expired', 'Hết hạn'),
        ],
        compute='_compute_warranty_status',
        store=True,
        tracking=True
    )
    
    owner_id = fields.Many2one(
        comodel_name='res.partner',
        string='Chủ sở hữu',
        required=True,
        tracking=True,
        help='Khách hàng sở hữu thiết bị'
    )
    
    owner_phone = fields.Char(
        string='Số điện thoại',
        related='owner_id.phone',
        readonly=True
    )
    
    brand_id = fields.Many2one(
        comodel_name='repair.brand',
        string='Hãng sản xuất',
        tracking=True
    )
    
    model_id = fields.Many2one(
        comodel_name='repair.model',
        string='Dòng máy',
        domain="[('brand_id', '=', brand_id)]",
        tracking=True
    )
    
    history_ids = fields.One2many(
        comodel_name='repair.history',
        inverse_name='device_id',
        string='Lịch sử sửa chữa'
    )
    
    repair_count = fields.Integer(
        string='Số lần sửa chữa',
        compute='_compute_repair_count',
        store=True
    )
    
    last_repair_date = fields.Date(
        string='Ngày sửa gần nhất',
        compute='_compute_last_repair_date',
        store=True
    )

    repair_order_ids = fields.One2many(
        comodel_name='repair.order',
        inverse_name='device_id',
        string='Phiếu sửa chữa'
    )

    @api.depends('purchase_date')
    def _compute_warranty_status(self):
        """Tính toán trạng thái bảo hành dựa trên ngày mua"""
        for record in self:
            if not record.purchase_date:
                record.warranty_status = False
                continue
            
            from datetime import timedelta
            purchase_date = fields.Datetime.from_string(record.purchase_date)
            warranty_end_date = purchase_date + timedelta(days=365)  # 12 tháng
            today = fields.Datetime.now()
            
            if today > warranty_end_date:
                record.warranty_status = 'expired'
            else:
                record.warranty_status = 'warranty'

    @api.depends('history_ids')
    def _compute_repair_count(self):
        """Đếm số lần sửa chữa"""
        for record in self:
            record.repair_count = len(record.history_ids)

    @api.depends('history_ids.date_log')
    def _compute_last_repair_date(self):
        """Tính ngày sửa gần nhất"""
        for record in self:
            if record.history_ids:
                dates = record.history_ids.mapped('date_log')
                record.last_repair_date = max(dates) if dates else False
            else:
                record.last_repair_date = False

    @api.model
    def create(self, vals):
        if vals.get('name', 'New') == 'New':
            vals['name'] = self.env['ir.sequence'].next_by_code('repair.device') or 'New'
        return super().create(vals)

    _sql_constraints = [
        ('serial_number_unique', 'UNIQUE(serial_number)', 'IMEI/Serial phải là duy nhất!'),
    ]
