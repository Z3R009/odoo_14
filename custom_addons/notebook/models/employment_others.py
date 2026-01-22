
from odoo import models, fields

class EmploymentOthers(models.Model):
    _name = 'employment.others'

    employment_form_id = fields.Many2one('form.model', string='Form', required=True)  
    
    company_name_o = fields.Char(string="Company Name")

    employment_status_o = fields.Selection([
        ('regular', 'Regular'),
        ('contractual', 'Contractual'),
        ('seasonal', 'Seasonal'),
        ('probationary', 'Probationary'),
    ], string='Employment Status', required=True ) 

    job_title_o = fields.Char(string="Position/Job Title/Length of Service")

    basic_monthly_salary_o = fields.Integer(string="Basic Monthly Salary")
    
    mandatory_deduction_o = fields.Float(string="Mandatory Deduction")