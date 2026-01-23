from odoo import models, fields

class FarmingExpense(models.Model):
    _name = 'farming.expense'

    farming_form_id = fields.Many2one('form.model', string='Form', required=True)
    farming_expense_name = fields.Char(string="Expense")
    farming_expense_amount = fields.Float(string="Amount")  