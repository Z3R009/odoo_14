
from odoo import models, fields

class Form(models.Model):
    _name = 'form.model'
    _description = 'Form'

    name = fields.Char(string="Name")

    business_id = fields.One2many(
        comodel_name='business.model',
        inverse_name='form_id',       
        string='Business'
    )

    others_id = fields.One2many(
    comodel_name='business.others',
    inverse_name='form_id',
    string='Others'
    )

    expense_ids = fields.One2many(
    comodel_name='business.expense',
    inverse_name='form_id',
    string='Expense'
    )


    business_total_gross_income = fields.Float(string="Total Gross Income")
    business_total_expenses = fields.Float(string="Total Expenses")
    business_total_net_income = fields.Float(string="Total Net Income")