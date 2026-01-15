from odoo import models, fields, api
from odoo.exceptions import UserError

class BillingPeriodWizard(models.TransientModel):
    _name = 'generate.billing.period.wizard'
    _description = 'Billing Period Filter Wizard'

    start_date = fields.Date(
        string="Start Date",
        required=True
    )

    end_date = fields.Date(
        string="End Date",
        required=True
    )

    def action_view_records(self):
        self.ensure_one()

        if self.start_date >= self.end_date:
            raise UserError("Start Date cannot be after or the same as End Date.")

        domain = [
            ('billing_date', '>=', self.start_date),
            ('billing_date', '<=', self.end_date),
        ]

        return {
            'type': 'ir.actions.act_window',
            'name': 'Billing Records',
            'res_model': 'payment.history',
            'view_mode': 'tree,form',
            'domain': domain,
            'context': {'create': False},
        }
