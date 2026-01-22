
from odoo import models, fields

class Employment(models.Model):
    _name = 'employment.model'
    _description = 'Employment'

    employment_form_id = fields.Many2one('form.model', string='Form', required=True)  
    
    company_name = fields.Char(string="Company Name")

    employment_status = fields.Selection([
        ('regular', 'Regular'),
        ('contractual', 'Contractual'),
        ('seasonal', 'Seasonal'),
        ('probationary', 'Probationary'),
    ], string='Employment Status', required=True ) 

    job_title = fields.Char(string="Position/Job Title/Length of Service")

    basic_monthly_salary = fields.Integer(string="Basic Monthly Salary")

    mandatory_deduction = fields.Float(string="Mandatory Deduction")
