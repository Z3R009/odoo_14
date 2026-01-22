from odoo import models, fields

class SelfEmployedOthers(models.Model):
    _name = 'self.employed.others'

    self_employed_form_id = fields.Many2one('form.model', string='Form', required=True)
    
    nature_of_work_o = fields.Char(string="Nature of Work")

    years_of_experience_o = fields.Integer(string="Years of Experience")

    average_income_o = fields.Float(string="Average Daily/Weekly Income")
