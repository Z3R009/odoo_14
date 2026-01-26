from odoo import api, models, fields

class BusinessExpense(models.Model):
    _name = 'business.expense'

    business_form_id = fields.Many2one('form.model', string='Form', required=True)
    business_expense_name = fields.Char(string="Expense")
    business_expense_amount = fields.Float(
        string="Amount",
        )
