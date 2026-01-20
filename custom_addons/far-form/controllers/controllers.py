# -*- coding: utf-8 -*-
# from odoo import http


# class Far-form(http.Controller):
#     @http.route('/far-form/far-form/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/far-form/far-form/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('far-form.listing', {
#             'root': '/far-form/far-form',
#             'objects': http.request.env['far-form.far-form'].search([]),
#         })

#     @http.route('/far-form/far-form/objects/<model("far-form.far-form"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('far-form.object', {
#             'object': obj
#         })
