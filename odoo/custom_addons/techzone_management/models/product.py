# -*- coding: utf-8 -*-

from odoo import models, fields, api


class ProductTemplate(models.Model):
    _inherit = 'product.template'

    is_repair_part = fields.Boolean(
        string='Là linh kiện sửa chữa',
        default=False,
        help='Đánh dấu sản phẩm này là linh kiện thay thế (Màn hình, Pin...) hoặc dịch vụ sửa chữa'
    )
