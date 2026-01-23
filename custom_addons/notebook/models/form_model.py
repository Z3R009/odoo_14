
from odoo import models, fields

class Form(models.Model):
    _name = 'form.model'
    _description = 'Form'

    name = fields.Char(string="Name")


    # farming section
    farming_crop_id = fields.One2many(
        comodel_name='farming.crop.model',        # the related model
        inverse_name='farming_form_id',      # the Many2one in farming.line 
        string='Crop'
    )

    farming_livestock_id = fields.One2many(
        comodel_name='farming.livestock.model',
        inverse_name='farming_form_id',
        string='Livestock'
    )

    farming_others_id = fields.One2many(
    comodel_name='farming.others',
    inverse_name='farming_form_id',
    string='Others'
    )

    farming_expense_id = fields.One2many(
    comodel_name='farming.expense',
    inverse_name='farming_form_id',
    string='Expense'
    )

    farming_total_crop_income = fields.Float(string="Total Crop Income")
    farming_total_livestock_income = fields.Float(string="Total Livestock Income")
    farming_total_others_income = fields.Float(string="Total Others Income")

    farming_total_gross_income = fields.Float(string="Total Gross Income")
    farming_total_expenses = fields.Float(string="Total Expenses")
    farming_total_net_income = fields.Float(string="Total Net Income")




    # business section

    business_id = fields.One2many(
        comodel_name='business.model',        # the related model
        inverse_name='business_form_id',      # the Many2one in business.line 
        string='Business'
    )

    business_others_id = fields.One2many(
    comodel_name='business.others',
    inverse_name='business_form_id',
    string='Others'
    )

    business_expense_id = fields.One2many(
    comodel_name='business.expense',
    inverse_name='business_form_id',
    string='Expense'
    )


    business_total_gross_income = fields.Float(string="Total Gross Income")
    business_total_expenses = fields.Float(string="Total Expenses")
    business_total_net_income = fields.Float(string="Total Net Income")


    # employment section

    employment_id = fields.One2many(
        comodel_name='employment.model',
        inverse_name='employment_form_id',       
        string='Employment'
    )

    employment_others_id = fields.One2many(
    comodel_name='employment.others',
    inverse_name='employment_form_id',
    string='Others'
    )

    employment_expense_id = fields.One2many(
    comodel_name='employment.expense',
    inverse_name='employment_form_id',
    string='Expense'
    )

    employment_total_gross_income = fields.Float(string="Total Gross Income")
    employment_total_expenses = fields.Float(string="Total Expenses")
    employment_total_net_income = fields.Float(string="Total Net Income")


# self-employed section

    self_employed_id = fields.One2many(
        comodel_name='self.employed.model',
        inverse_name='self_employed_form_id',       
        string='Self Employment'
    )

    self_employed_others_id = fields.One2many(
    comodel_name='self.employed.others',
    inverse_name='self_employed_form_id',
    string='Others'
    )

    self_employed_expense_id = fields.One2many(
    comodel_name='self.employed.expense',
    inverse_name='self_employed_form_id',
    string='Expense'
    )

    self_employed_total_gross_income = fields.Float(string="Total Gross Income")
    self_employed_total_expenses = fields.Float(string="Total Expenses")
    self_employed_total_net_income = fields.Float(string="Total Net Income")