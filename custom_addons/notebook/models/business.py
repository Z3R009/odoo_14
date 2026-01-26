
from odoo import api, models, fields

class Business(models.Model):
    _name = 'business.model'
    _description = 'Business'

    business_form_id = fields.Many2one('form.model', string='Form', required=False, ondelete='cascade')  
    

    business_type = fields.Selection([
        ('buy_and_sell', 'Buy and Sell'),
        ('sari_sari_store', 'Sari - Sari Store'),
        ('services', 'Services'),
    ], string='Business Type', required=True ) 

    business_location = fields.Char(
        string="Business Location", 
        store=True
    )

    employee_count = fields.Integer(
        string="Number of Employees",
        store=True
    )

    sales = fields.Float(string="Sales")

    sales_cost = fields.Float(
        string="Cost of Sales",
        store=True
    )

    gross_sales = fields.Float(
        string="Gross Sales",
        compute = 'compute_gross_income',
        store=True
    )


    @api.depends('sales', 'sales_cost')
    def compute_gross_income(self):
        for record in self:
            record.gross_sales = record.sales - record.sales_cost 