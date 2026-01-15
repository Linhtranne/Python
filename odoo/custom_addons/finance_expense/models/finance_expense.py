# -*- coding: utf-8 -*- 

from odoo import models, fields
class FinanceExpense(models.Model):
    _name = 'finance.expense'
    _description = 'Finance Expense Management'
    _rec_name = 'name'

    name = fields.Char(string='Expense Name', required=True, help='Nội dung chi tiêu')
    expense_type = fields.Selection([('travel', 'di chuyển'), ('food', 'ăn uống'), ('other', 'Khác')], string='Expense Type', default='travel', help='Lựa chọn chi tiêu')
    amount = fields.Float(string='Amount', required=True, help='Số tiền yêu cầu')
    expense_date = fields.Date(string='Expense Date', required=True, help='Ngày chi tiêu')
    is_paid =  fields.Boolean(string='Is Paid', default=False, help='Đã thanh toán chưa')
    approval_note = fields.Text(string='Approval Note', help='Ghi chú duyệt chi')