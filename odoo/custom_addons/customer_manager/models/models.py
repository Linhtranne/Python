# -*- coding: utf-8 -*-

from odoo import models, fields, api
class CustomerManager(models.Model):
    _inherit = 'res.partner'
    facebook_id = fields.Char(string="Facebook ID")
class ArchiveCustomer(models.Model):
    _inherit = 'res.partner'
    _name = 'archive.customer'

    facebook_id = fields.Char(string="Facebook ID")
    zalo_id = fields.Char(string="Zalo ID")


