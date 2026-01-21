from odoo import models, fields


class FinancingAssessment(models.Model):
    _name = 'financing.assessment'
    _description = 'Financing Assessment'

    business_line_ids = fields.One2many(
        'financing.assessment.business.line',
        'assessment_id',
        string='Business Lines'
    )
