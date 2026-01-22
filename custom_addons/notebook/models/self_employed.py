
from odoo import models, fields

class SelfEmployed(models.Model):
    _name = 'self.employed.model'
    _description = 'Self Employed'

    self_employed_form_id = fields.Many2one('form.model', string='Form', required=True)  

    nature_of_work = fields.Char(string="Nature of Work")

    years_of_experience = fields.Integer(string="Years of Experience")

    average_income = fields.Float(string="Average Daily/Weekly Income")
