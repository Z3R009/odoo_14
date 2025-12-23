# -*- coding: utf-8 -*-
# from odoo import http


# class SalesTracker(http.Controller):
#     @http.route('/sales_tracker/sales_tracker/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/sales_tracker/sales_tracker/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('sales_tracker.listing', {
#             'root': '/sales_tracker/sales_tracker',
#             'objects': http.request.env['sales_tracker.sales_tracker'].search([]),
#         })

#     @http.route('/sales_tracker/sales_tracker/objects/<model("sales_tracker.sales_tracker"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('sales_tracker.object', {
#             'object': obj
#         })
