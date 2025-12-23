# -*- coding: utf-8 -*-
# from odoo import http


# class WaterBilling(http.Controller):
#     @http.route('/water_billing/water_billing/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/water_billing/water_billing/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('water_billing.listing', {
#             'root': '/water_billing/water_billing',
#             'objects': http.request.env['water_billing.water_billing'].search([]),
#         })

#     @http.route('/water_billing/water_billing/objects/<model("water_billing.water_billing"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('water_billing.object', {
#             'object': obj
#         })
