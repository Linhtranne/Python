# -*- coding: utf-8 -*-
# from odoo import http


# class CustomerManager(http.Controller):
#     @http.route('/customer_manager/customer_manager', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/customer_manager/customer_manager/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('customer_manager.listing', {
#             'root': '/customer_manager/customer_manager',
#             'objects': http.request.env['customer_manager.customer_manager'].search([]),
#         })

#     @http.route('/customer_manager/customer_manager/objects/<model("customer_manager.customer_manager"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('customer_manager.object', {
#             'object': obj
#         })

