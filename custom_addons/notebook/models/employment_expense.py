from odoo import models, fields

class EmploymentExpense(models.Model):
    _name = 'employment.expense'

    employment_form_id = fields.Many2one('form.model', string='Form', required=True)
    employment_expense_name = fields.Char(string="Expense")
    employment_expense_amount = fields.Float(string="Amount")