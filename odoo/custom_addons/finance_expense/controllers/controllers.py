# -*- coding: utf-8 -*-
# from odoo import http


# class FinanceExpense(http.Controller):
#     @http.route('/finance_expense/finance_expense', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/finance_expense/finance_expense/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('finance_expense.listing', {
#             'root': '/finance_expense/finance_expense',
#             'objects': http.request.env['finance_expense.finance_expense'].search([]),
#         })

#     @http.route('/finance_expense/finance_expense/objects/<model("finance_expense.finance_expense"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('finance_expense.object', {
#             'object': obj
#         })

