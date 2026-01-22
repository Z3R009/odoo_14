
from odoo import models, fields

class Business(models.Model):
    _name = 'business.model'
    _description = 'Business'

    form_id = fields.Many2one('form.model', string='Form', required=True)  
    

    business_type = fields.Selection([
        ('buy_and_sell', 'Buy and Sell'),
        ('sari_sari_store', 'Sari - Sari Store'),
        ('services', 'Services'),
    ], string='Business Type', required=True ) 
    business_location = fields.Char(string="Business Location")

    employee_count = fields.Integer(string="Number of Employees")

    sales_cost = fields.Float(string="Cost of Sales")

    gross_sales = fields.Float(string="Gross Sales")
