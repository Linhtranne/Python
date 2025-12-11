# -*- coding: utf-8 -*-
# from odoo import http


# class SchoolManagemnet(http.Controller):
#     @http.route('/school_managemnet/school_managemnet', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/school_managemnet/school_managemnet/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('school_managemnet.listing', {
#             'root': '/school_managemnet/school_managemnet',
#             'objects': http.request.env['school_managemnet.school_managemnet'].search([]),
#         })

#     @http.route('/school_managemnet/school_managemnet/objects/<model("school_managemnet.school_managemnet"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('school_managemnet.object', {
#             'object': obj
#         })

