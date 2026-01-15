# -*- coding: utf-8 -*-
# from odoo import http


# class TrainingCourse(http.Controller):
#     @http.route('/training_course/training_course', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/training_course/training_course/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('training_course.listing', {
#             'root': '/training_course/training_course',
#             'objects': http.request.env['training_course.training_course'].search([]),
#         })

#     @http.route('/training_course/training_course/objects/<model("training_course.training_course"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('training_course.object', {
#             'object': obj
#         })

