from odoo import models, fields

class SelfEmployedExpense(models.Model):
    _name = 'self.employed.expense'

    self_employed_form_id = fields.Many2one('form.model', string='Form', required=True)
    self_employed_expense_name = fields.Char(string="Expense")
    self_employed_expense_amount = fields.Float(string="Amount")
