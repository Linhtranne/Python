# -*- coding: utf-8 -*-

from odoo import models, fields


class Book(models.Model):
    _name = 'bookstore.book'
    _description = 'Book Management'
    _rec_name = 'title'

    title = fields.Char(string='Title', required=True, help='Book title')
    author = fields.Char(string='Author', required=True, help='Book author')
    price = fields.Float(string='Price', help='Book price')
    publish_date = fields.Date(string='Publish Date', help='Book publish date')
