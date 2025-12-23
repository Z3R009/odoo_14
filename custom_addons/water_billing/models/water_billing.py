from odoo import models, fields, api
from odoo.exceptions import ValidationError
from odoo.exceptions import UserError

class WaterBilling(models.Model):
    _name = "water.billing"
    _description = "Water Billing"

    transaction_id = fields.Char(
    string="Transaction ID",
    required=True,
    readonly=True,
    store=True,
    default=lambda self: self.env['ir.sequence'].next_by_code('water.billing')
)

    member_id = fields.Many2one(
        'water.member',
        string="Customer Name",
        required=True
    )
    billing_date = fields.Date(
        string="Billing Date",
        default=fields.Date.today
    )
    previous_reading = fields.Float(
        string="Previous Reading"
    )
    
    current_reading = fields.Float(string="Current Reading")

    usage = fields.Float(string="Usage")
    
    amount = fields.Float(
        string="Total Amount",
        compute="_compute_amount",
        store=True
    )
    # paid = fields.Boolean(
    #     string="Paid",
    #     default=False
    # )

    payment_amount = fields.Float(string="Payment Amount")

    # invoice_id = fields.Many2one(
    # 'account.move',
    # string="Invoice",
    # readonly=True
    # )


    @api.depends('usage')
    def _compute_amount(self):
        for record in self:
            record.amount = record.usage * 15  # rate per m³

    @api.model
    def create(self, vals):
        """Set previous reading automatically from last billing record of this member"""
        if 'member_id' in vals:
            last_billing = self.search(
                [('member_id', '=', vals['member_id'])],
                order='billing_date desc', limit=1
            )
            vals['previous_reading'] = last_billing.current_reading if last_billing else 0
        # If usage is provided, copy to current_reading
        if 'usage' in vals:
            vals['current_reading'] = vals['previous_reading'] + vals['usage']
        return super(WaterBilling, self).create(vals)
    


    
    def action_pay(self):
        for record in self:
            if record.payment_amount < record.amount:
                raise ValidationError(
                    f"Payment amount ({record.payment_amount}) is less than the billed amount ({record.amount})!"
                )
            record.paid = True

    def action_generate_report(self):
        # Generate a PDF report of all billing records
        records = self.search([])  # you can add filters if needed

        if not records:
            raise UserError("No billing records found to generate a report.")

        # Call the QWeb report (must be defined in XML)
        return self.env.ref('water_billing.action_water_billing_report').report_action(records)
