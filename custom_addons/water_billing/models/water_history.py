# from odoo import models, fields

# class WaterBilling(models.Model):
#     _name = "water.billing"
#     _description = "Water Billing"

#     member_id = fields.Many2one("water.member", string="Member")
#     billing_date = fields.Date(string="Billing Date")
#     usage = fields.Float(string="Usage (m³)")
#     amount = fields.Float(string="Amount")
#     paid = fields.Boolean(string="Paid")