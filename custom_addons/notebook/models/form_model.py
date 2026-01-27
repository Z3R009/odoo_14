
from odoo import api, models, fields

class Form(models.Model):
    _name = 'form.model'
    _description = 'Form'

    partner_id = fields.Many2one(
    'res.partner',
    string='Name',
    required=True
    )



    # farming section
    farming_crop_id = fields.One2many(
        comodel_name='farming.crop.model',        # the related model
        inverse_name='farming_form_id',      # the Many2one in farming.line 
        string='Crop',
        ondelete='cascade'
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
        string='Business',
        ondelete='cascade'
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

    business_total_income = fields.Float(
        string="Total Income",
        compute='_compute_business_total_income',
    )

    business_total_others_income = fields.Float(
        string="Total Others Income",
        compute='_compute_business_total_others_income',
        store=True,
    )


    business_total_gross_income = fields.Float(
        string="Total Gross Income",
        store=True,
        compute='_compute_business_total_gross_income',
    )

    business_total_expenses = fields.Float(
        string="Total Expenses",
        compute='_compute_business_total_expenses',
        store=True,
        )
    
    business_total_net_income = fields.Float(
        string="Total Net Income",
        store=True,
        compute='_compute_business_totals',
    )


    # employment section

    employment_id = fields.One2many(
        comodel_name='employment.model',
        inverse_name='employment_form_id',       
        string='Employment',
        ondelete='cascade'
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

    employment_total_income = fields.Float(
        string="Total Income",
        compute='_compute_employment_total_income',
        store=True,
    )

    employment_total_others_income = fields.Float(
        string="Total Others Income",
        compute='_compute_employment_total_others_income',
        store=True,
    )

    employment_total_gross_income = fields.Float(
        string="Total Gross Income",
        compute='_compute_employment_total_gross_income',
        store=True,
    )

    employment_total_expenses = fields.Float(
        string="Total Expenses",
        compute='_compute_employment_total_expenses',
        store=True,
    )

    employment_total_net_income = fields.Float(
        string="Total Net Income",
        compute='_compute_employment_totals',
        store=True,
    )


# self-employed section

    self_employed_id = fields.One2many(
        comodel_name='self.employed.model',
        inverse_name='self_employed_form_id',       
        string='Self Employment',
        ondelete='cascade'
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



    #business calculations

    # business income calculation
    @api.depends('business_id.gross_sales')
    def _compute_business_total_income(self):
        for record in self:
            record.business_total_income = sum(
                record.business_id.mapped('gross_sales')
            )

    #business others income calculation
    @api.depends('business_others_id.gross_sales_o')
    def _compute_business_total_others_income(self):
        for record in self:
            record.business_total_others_income = sum(
                record.business_others_id.mapped('gross_sales_o')
            )


    #business expense calculation
    @api.depends('business_expense_id.business_expense_amount')
    def _compute_business_total_expenses(self):
        for record in self:
            record.business_total_expenses = sum(
                record.business_expense_id.mapped('business_expense_amount')
            )

    # business income and others total
    @api.depends('business_total_income', 'business_total_others_income')
    def _compute_business_total_gross_income(self):
        for record in self:
            record.business_total_gross_income = (
                record.business_total_income +
                record.business_total_others_income
            )

    @api.depends(
    'business_total_income',
    'business_total_others_income',
    'business_total_expenses'
    )
    def _compute_business_totals(self):
        for record in self:
            gross_income = (
                record.business_total_income +
                record.business_total_others_income
            )

            record.business_total_gross_income = gross_income
            record.business_total_net_income = (
                gross_income - record.business_total_expenses
            )


    # employment calculations

    # employment income calculation
    @api.depends('employment_id.basic_monthly_salary')
    def _compute_employment_total_income(self):
        for record in self:
            record.employment_total_income = sum(
                record.employment_id.mapped('basic_monthly_salary')
            )


    # employment others income calculation
    @api.depends('employment_others_id.basic_monthly_salary_o')
    def _compute_employment_total_others_income(self):
        for record in self:
            record.employment_total_others_income = sum(
                record.employment_others_id.mapped('basic_monthly_salary_o')
            )


    # employment expense calculation
    @api.depends('employment_expense_id.employment_expense_amount')
    def _compute_employment_total_expenses(self):
        for record in self:
            record.employment_total_expenses = sum(
                record.employment_expense_id.mapped('employment_expense_amount')
            )

    # employment income and others total
    @api.depends('employment_total_income', 'employment_total_others_income')
    def _compute_employment_total_gross_income(self):
        for record in self:
            record.employment_total_gross_income = (
                record.employment_total_income +
                record.employment_total_others_income
            )

    @api.depends(
    'employment_total_income',
    'employment_total_others_income',
    'employment_total_expenses'
    )
    def _compute_employment_totals(self):
        for record in self:
            gross_income = (
                record.employment_total_income +
                record.employment_total_others_income
            )

            record.employment_total_gross_income = gross_income
            record.employment_total_net_income = (
                gross_income - record.employment_total_expenses
            )
        for record in self:
            record.business_total_gross_income = (
                record.employment_total_net_income +
                record.business_total_others_income
            )