from odoo import api, models, fields

class BusinessOthers(models.Model):
    _name = 'business.others'

    business_form_id = fields.Many2one('form.model', string='Form', required=True)
    
    business_type_o = fields.Char(string='Business Type', required=True ) 

    business_location_o = fields.Char(string="Business Location")

    employee_count_o = fields.Integer(string="Number of Employees")

    sales_o = fields.Float(string="Sales")

    sales_cost_o = fields.Float(string="Cost of Sales")

    gross_sales_o = fields.Float(
        string="Gross Sales",
        compute = 'compute_gross_income',
        )

    @api.depends('sales_o', 'sales_cost_o')
    def compute_gross_income(self):
        for record in self:
            record.gross_sales_o = record.sales_o - record.sales_cost_o 