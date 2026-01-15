# -*- coding: utf-8 -*-
from odoo import models, fields
class HrJobPosition(models.Model):
    _name = 'hr.job.position'
    _description = 'Vị trí công việc'

    name = fields.Char(string='Tên vị trí', required=True)
    description = fields.Text(string='Mô tả công việc')
