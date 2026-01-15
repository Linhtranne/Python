# -*- coding: utf-8 -*-
# from odoo import http


# class Hr-candidate(http.Controller):
#     @http.route('/hr-candidate/hr-candidate', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/hr-candidate/hr-candidate/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('hr-candidate.listing', {
#             'root': '/hr-candidate/hr-candidate',
#             'objects': http.request.env['hr-candidate.hr-candidate'].search([]),
#         })

#     @http.route('/hr-candidate/hr-candidate/objects/<model("hr-candidate.hr-candidate"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('hr-candidate.object', {
#             'object': obj
#         })

