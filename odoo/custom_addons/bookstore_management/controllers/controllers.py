# -*- coding: utf-8 -*-
# from odoo import http


# class BookstoreManagement(http.Controller):
#     @http.route('/bookstore_management/bookstore_management', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/bookstore_management/bookstore_management/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('bookstore_management.listing', {
#             'root': '/bookstore_management/bookstore_management',
#             'objects': http.request.env['bookstore_management.bookstore_management'].search([]),
#         })

#     @http.route('/bookstore_management/bookstore_management/objects/<model("bookstore_management.bookstore_management"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('bookstore_management.object', {
#             'object': obj
#         })

