from odoo import models, fields

class BusinessOthers(models.Model):
    _name = 'business.others'

    business_form_id = fields.Many2one('form.model', string='Form', required=True)
    
    business_type_o = fields.Char(string='Business Type', required=True ) 

    business_location_o = fields.Char(string="Business Location")

    employee_count_o = fields.Integer(string="Number of Employees")

    sales_cost_o = fields.Float(string="Cost of Sales")

    gross_sales_o = fields.Float(string="Gross Sales")
