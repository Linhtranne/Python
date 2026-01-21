# -*- coding: utf-8 -*-

from odoo import models, fields, api, _
from odoo.exceptions import ValidationError


class RepairOrder(models.Model):
    _name = 'repair.order'
    _description = 'Phiếu sửa chữa'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _order = 'name desc'

    name = fields.Char(
        string='Mã phiếu',
        required=True,
        readonly=True,
        copy=False,
        default='New',
        help='Mã phiếu sửa chữa tự động'
    )
    
    state = fields.Selection(
        string='Trạng thái',
        selection=[
            ('draft', 'Mới'),
            ('diagnose', 'Kiểm tra'),
            ('quoted', 'Báo giá'),
            ('in_progress', 'Đang sửa'),
            ('done', 'Hoàn thành'),
            ('returned', 'Trả máy'),
            ('cancel', 'Đã hủy'),
        ],
        default='draft',
        tracking=True,
        required=True
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
        required=True,
        tracking=True,
        domain="[('owner_id', '=', partner_id)]"
    )
    
    technician_id = fields.Many2one(
        comodel_name='res.users',
        string='Kỹ thuật viên',
        tracking=True,
        default=lambda self: self.env.user
    )
    
    date_receipt = fields.Date(
        string='Ngày tiếp nhận',
        required=True,
        default=fields.Date.today,
        tracking=True
    )
    
    deadline = fields.Date(
        string='Hạn trả máy',
        required=True,
        tracking=True
    )
    
    amount_total = fields.Monetary(
        string='Tổng tiền',
        compute='_compute_amount_total',
        store=True,
        currency_field='currency_id'
    )
    
    currency_id = fields.Many2one(
        comodel_name='res.currency',
        string='Tiền tệ',
        default=lambda self: self.env.company.currency_id
    )
    
    line_ids = fields.One2many(
        comodel_name='repair.line',
        inverse_name='order_id',
        string='Chi tiết vật tư/công'
    )

    brand_id = fields.Many2one(
        related='device_id.brand_id',
        string='Hãng sản xuất',
        store=True,
        readonly=True
    )



    @api.depends('line_ids.price_subtotal')
    def _compute_amount_total(self):
        """Tính tổng tiền từ các dòng chi tiết"""
        for record in self:
            record.amount_total = sum(record.line_ids.mapped('price_subtotal'))

    @api.model
    def create(self, vals):
        """Tạo mã phiếu tự động"""
        if vals.get('name', 'New') == 'New':
            vals['name'] = self.env['ir.sequence'].next_by_code('repair.order') or 'New'
        return super().create(vals)

    def action_diagnose(self):
        """Chuyển sang trạng thái Kiểm tra"""
        self.write({'state': 'diagnose'})

    def action_quote(self):
        """Chuyển sang trạng thái Báo giá"""
        self.write({'state': 'quoted'})

    def action_start(self):
        """Chuyển sang trạng thái Đang sửa"""
        self.write({'state': 'in_progress'})

    def action_done(self):
        """Chuyển sang trạng thái Hoàn thành"""
        self.write({'state': 'done'})
        # Cập nhật ngày sửa gần nhất cho thiết bị
        if self.device_id:
            self.device_id.last_repair_date = fields.Date.today()

    def action_return(self):
        """Chuyển sang trạng thái Trả máy"""
        self.write({'state': 'returned'})

    def action_cancel(self):
        """Hủy phiếu"""
        if self.state in ('in_progress', 'done'):
            raise ValidationError('Không thể hủy phiếu đang sửa hoặc đã hoàn thành!')
        self.write({'state': 'cancel'})

    @api.onchange('partner_id')
    def _onchange_partner_id(self):
        """Gợi ý danh sách thiết bị của khách hàng"""
        if self.partner_id:
            return {
                'domain': {
                    'device_id': [('owner_id', '=', self.partner_id.id)]
                }
            }

    @api.constrains('deadline', 'date_receipt')
    def _check_deadline(self):
        """Kiểm tra ngày hẹn trả phải >= ngày tiếp nhận"""
        for record in self:
            if record.deadline and record.date_receipt:
                if record.deadline < record.date_receipt:
                    raise ValidationError('Ngày hẹn trả máy phải lớn hơn hoặc bằng ngày tiếp nhận!')


class RepairLine(models.Model):
    _name = 'repair.line'
    _description = 'Chi tiết vật tư/công'

    order_id = fields.Many2one(
        comodel_name='repair.order',
        string='Phiếu sửa chữa',
        required=True,
        ondelete='cascade'
    )
    
    product_id = fields.Many2one(
        comodel_name='product.product',
        string='Linh kiện/Dịch vụ',
        required=True,
        domain="[('is_repair_part', '=', True)]"
    )
    
    product_uom_qty = fields.Float(
        string='Số lượng',
        required=True,
        default=1.0
    )
    
    price_unit = fields.Float(
        string='Đơn giá',
        required=True
    )
    
    price_subtotal = fields.Monetary(
        string='Thành tiền',
        compute='_compute_subtotal',
        store=True,
        currency_field='currency_id'
    )
    
    currency_id = fields.Many2one(
        related='order_id.currency_id',
        string='Tiền tệ',
        readonly=True
    )

    display_type = fields.Selection(
        selection=[('line', 'Line'), ('section', 'Section'), ('note', 'Note')],
        default='line',
        string='Loại dòng',
        help='Section/Note dùng cho mục tiêu hiển thị, không tính vào tổng tiền'
    )

    is_repair_part = fields.Boolean(
        related='product_id.product_tmpl_id.is_repair_part',
        string="Is a Repair Part",
        store=True
    )

    @api.depends('product_uom_qty', 'price_unit', 'display_type')
    def _compute_subtotal(self):
        """Tính thành tiền = số lượng * đơn giá (chỉ tính dòng type 'line')"""
        for record in self:
            if record.display_type == 'line':
                record.price_subtotal = record.product_uom_qty * record.price_unit
            else:
                record.price_subtotal = 0

    @api.onchange('product_id')
    def _onchange_product_id(self):
        """Tự động điền giá bán khi chọn linh kiện"""
        if self.product_id:
            self.price_unit = self.product_id.list_price

    @api.constrains('product_uom_qty')
    def _check_qty(self):
        """Kiểm tra số lượng không được âm"""
        for record in self:
            if record.product_uom_qty < 0:
                raise ValidationError('Số lượng linh kiện không được âm!')
