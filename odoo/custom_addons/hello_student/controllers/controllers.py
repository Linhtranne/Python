# -*- coding: utf-8 -*-
# from odoo import http


# class HelloStudent(http.Controller):
#     @http.route('/hello_student/hello_student', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/hello_student/hello_student/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('hello_student.listing', {
#             'root': '/hello_student/hello_student',
#             'objects': http.request.env['hello_student.hello_student'].search([]),
#         })

#     @http.route('/hello_student/hello_student/objects/<model("hello_student.hello_student"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('hello_student.object', {
#             'object': obj
#         })

