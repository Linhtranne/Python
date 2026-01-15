# -*- coding: utf-8 -*-

from odoo import models, fields, api
from datetime import timedelta
import odoo.exceptions as ValidationError


class LibraryCategory(models.Model):
    _name = 'library.category'
    _description = 'Thể loại sách'

    name = fields.Char(string="Tên thể loại", required=True)


class LibraryAuthor(models.Model):
    _name = 'library.author'
    _description = 'Tác giả'

    name = fields.Char(string="Tên tác giả", required=True)
    bio = fields.Text(string="Tiểu sử")


class LibraryLoan(models.Model):
    _name = 'library.loan'
    _description = 'Lịch sử mượn sách'

    borrower_name = fields.Char(string="Tên người mượn")
    borrow_date = fields.Date(string="Ngày mượn", default=fields.Date.today)
    return_date = fields.Date(string="Ngày trả")
    is_returned = fields.Boolean(string="Đã trả chưa")
    duration = fields.Integer(string="Số ngày mượn", compute='_compute_duration', store=True)

    # Liên kết ngược về book
    book_id = fields.Many2one('library.book', string="Sách")

    @api.depends('borrow_date', 'return_date')
    def _compute_duration(self):
        for record in self:
            if record.return_date and record.borrow_date:
                record.duration = (record.return_date - record.borrow_date).days
            else:
                record.duration = 0

    @api.onchange('borrow_date')
    def _onchange_borrow_date(self):
        if self.borrow_date:
            self.return_date = self.borrow_date + timedelta(days=7)

    @api.constrains('borrow_date', 'return_date')
    def _constrains_fieldname(self):
        for record in self:
                if record.return_date < record.borrow_date:
                    raise ValidationError("Ngày trả phải sau ngày mượn")
    @api.constrains('book_id')
    def _constrains_fieldname(self):
        pass

class LibraryBook(models.Model):
    _name = 'library.book'
    _description = 'Sách'

    name = fields.Char(string="Tên sách", required=True)
    isbn = fields.Char(string="Mã ISBN")
    state = fields.Selection([
        ('draft', 'Mới nhập'),
        ('available', 'Có sẵn'),
        ('borrowed', 'Đang mượn'),
        ('lost', 'Đã mất')
    ], string="Tình trạng", default='draft')
    condition = fields.Selection([
        ('0', 'Kém'),
        ('1', 'TB'),
        ('2', 'Tốt'),
        ('3', 'Mới')
    ], string="Độ mới sách", default='3')
    purchase_price = fields.Integer(string="Giá nhập")
    purchase_date = fields.Date(string="Ngày nhập sách", default=fields.Date.today)
    notes = fields.Text(string="Ghi chú")

    # Computed fields
    short_description = fields.Char(string="Mô tả ngắn", compute='_compute_short_description', store=True)
    days_since_purchase = fields.Integer(string="Tuổi đời sách (ngày)", compute='_compute_days_since_purchase', store=True)
    total_loans = fields.Integer(string="Tổng số lần mượn", compute='_compute_total_loans', store=True)

    # Relationships
    category_id = fields.Many2one('library.category', string="Thể loại")
    author_ids = fields.Many2many('library.author', string="Tác giả")
    loan_ids = fields.One2many('library.loan', 'book_id', string="Lịch sử mượn trả")
    _sql_constraints = [
        ('isbn_unique', 'unique(isbn)', 'Mã ISBN phải là duy nhất.'),
        ('library_book_positive_price', 'CHECK(purchase_price >= 0)', 'Giá nhập sách phải là số dương.')
    ]

    @api.depends('name', 'author_ids', 'isbn')
    def _compute_short_description(self):
        for record in self:
            authors = ', '.join(record.author_ids.mapped('name')) if record.author_ids else ''
            record.short_description = f"{record.name} - {authors} ({record.isbn})"

    @api.depends('purchase_date')
    def _compute_days_since_purchase(self):
        today = fields.Date.today()
        for record in self:
            if record.purchase_date:
                record.days_since_purchase = (today - record.purchase_date).days
            else:
                record.days_since_purchase = 0

    @api.depends('loan_ids')
    def _compute_total_loans(self):
        for record in self:
            record.total_loans = len(record.loan_ids)

    @api.onchange('state')
    def _onchange_state(self):
        if self.state == 'lost':
            self.condition = '0'

    @api.onchange('isbn')
    def _onchange_isbn(self):
        if self.isbn and len(self.isbn) > 13:
            return {
                'warning': {
                    'title': 'Mã ISBN không chuẩn',
                    'message': 'Mã ISBN không chuẩn (thường tối đa 13 số)'
                }
            }

    @api.onchange('category_id')
    def _onchange_category_id(self):
        if self.category_id:
            self.notes = f"Sách thuộc thể loại {self.category_id.name} - Vui lòng xếp đúng kệ."
