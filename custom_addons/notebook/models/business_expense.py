from odoo import models, fields

class BusinessExpense(models.Model):
    _name = 'business.expense'

    form_id = fields.Many2one('form.model', string='Form', required=True)
    expense_name = fields.Char(string="Expense")
    expense_amount = fields.Float(string="Amount")
