# -*- coding: utf-8 -*-

from odoo import models, fields, api


class ResPartner(models.Model):
    _inherit = 'res.partner'

    device_ids = fields.One2many(
        comodel_name='repair.device',
        inverse_name='owner_id',
        string='Danh sách thiết bị sở hữu'
    )
    
    device_count = fields.Integer(
        string='Số lượng thiết bị',
        compute='_compute_device_count',
        store=True
    )

    @api.depends('device_ids')
    def _compute_device_count(self):
        """Đếm số lượng thiết bị của khách hàng"""
        for record in self:
            record.device_count = len(record.device_ids)
