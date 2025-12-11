# -*- coding: utf-8 -*-
# from odoo import http


# class StudentScore(http.Controller):
#     @http.route('/student_score/student_score', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/student_score/student_score/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('student_score.listing', {
#             'root': '/student_score/student_score',
#             'objects': http.request.env['student_score.student_score'].search([]),
#         })

#     @http.route('/student_score/student_score/objects/<model("student_score.student_score"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('student_score.object', {
#             'object': obj
#         })

