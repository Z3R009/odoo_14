# -*- coding: utf-8 -*-
# from odoo import http


# class FieldsContacts(http.Controller):
#     @http.route('/fields_contacts/fields_contacts/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/fields_contacts/fields_contacts/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('fields_contacts.listing', {
#             'root': '/fields_contacts/fields_contacts',
#             'objects': http.request.env['fields_contacts.fields_contacts'].search([]),
#         })

#     @http.route('/fields_contacts/fields_contacts/objects/<model("fields_contacts.fields_contacts"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('fields_contacts.object', {
#             'object': obj
#         })
