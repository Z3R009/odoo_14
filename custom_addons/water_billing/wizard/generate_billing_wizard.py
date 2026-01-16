from odoo import models, fields, api
from odoo.exceptions import UserError

class GenerateBillingWizard(models.TransientModel):
    _name = 'generate.billing.wizard'
    _description = 'Generate Water Billing'

    start_date = fields.Date(string="Start Date", store=True, required=True)
    end_date = fields.Date(string="End Date", store=True, required=True)

    billing_date = fields.Date(
        string="Billing Date",
        default=fields.Date.today
    )

    def action_generate_billing(self):
        self.ensure_one()

        if self.start_date > self.end_date:
            raise UserError("Start Date cannot be after End Date.")

        partners = self.env['res.partner'].search([
            ('is_water_member', '=', True)
        ])

        ReadMeter = self.env['read.meter']

        for partner in partners:
            existing_reading = ReadMeter.search([
                ('member_id', '=', partner.id),
                ('start_date', '=', self.start_date),
                ('end_date', '=', self.end_date),
            ], limit=1)

# if existing reading is found skip that customer
            if existing_reading:
                continue
            

            ReadMeter.create({
                'member_id': partner.id,
                'start_date': self.start_date,  
                'end_date': self.end_date,           
                'billing_date': self.billing_date,
                'usage': 0.0,
            })

        return {'type': 'ir.actions.client', 'tag': 'reload'}
