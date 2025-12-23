# -*- coding: utf-8 -*-

# from odoo import models, fields, api


# class water_billing(models.Model):
#     _name = 'water_billing.water_billing'
#     _description = 'water_billing.water_billing'

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100
