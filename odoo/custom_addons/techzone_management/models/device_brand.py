# -*- coding: utf-8 -*-

from odoo import models, fields, api


class RepairBrand(models.Model):
    _name = 'repair.brand'
    _description = 'Hãng sản xuất'
    _order = 'name'

    name = fields.Char(
        string='Tên hãng',
        required=True,
        help='Tên hãng sản xuất (Apple, Samsung, Dell...)'
    )
    
    icon = fields.Binary(
        string='Icon',
        attachment=True,
        help='Icon của hãng'
    )
    
    model_ids = fields.One2many(
        comodel_name='repair.model',
        inverse_name='brand_id',
        string='Danh sách dòng máy'
    )


class RepairModel(models.Model):
    _name = 'repair.model'
    _description = 'Dòng máy'
    _order = 'name'

    name = fields.Char(
        string='Tên dòng máy',
        required=True,
        help='Tên dòng máy (iPhone 13, Galaxy S24...)'
    )
    
    release_year = fields.Integer(
        string='Năm phát hành',
        help='Năm phát hành dòng máy'
    )
    
    brand_id = fields.Many2one(
        comodel_name='repair.brand',
        string='Hãng sản xuất',
        required=True,
        ondelete='cascade',
        help='Hãng sản xuất của dòng máy'
    )
    
    device_ids = fields.One2many(
        comodel_name='repair.device',
        inverse_name='model_id',
        string='Danh sách thiết bị'
    )
