from odoo import models, fields

class FinancingAssessmentBusinessLine(models.Model):
    _name = 'financing.assessment.business.line'
    _description = 'Business Line'

    assessment_id = fields.Many2one(
        'financing.assessment',
        string='Assessment',
        ondelete='cascade'
    )

    business_type = fields.Char(string='Type of Business')
    location = fields.Float(string='Location')
    employee_count = fields.Char(string='Number of Employees')
    cost_of_sales = fields.Char(string='Cost of Sales')
    gross_sales = fields.Char(string='Gross Sales')
    total_sales = fields.Char(string='Total Sales')
