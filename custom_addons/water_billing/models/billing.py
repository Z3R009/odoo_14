from odoo import models, fields, api
from odoo.exceptions import ValidationError


class PayBills(models.Model):
    _name = "pay.bills"
    _description = "Pay Bills"


    transaction_id = fields.Char(
    string="Transaction ID",
    required=True,
    store=True,
    readonly=True,
    default=lambda self: self.env['ir.sequence'].next_by_code('pay.bills')
    )

    reading_id = fields.Many2one(
    'read.meter',
    string="Reading ID",
    required=True,
    ondelete='cascade'
    )


    reading_code = fields.Char(
    string="Reading ID",
    related='reading_id.reading_id',
    readonly=True
    )


    member_id = fields.Many2one(
        'res.partner',
        string="Customer",
        required=True,
        domain="[('is_water_member','=',True)]",
        ondelete='cascade'
    )


    billing_date = fields.Date(
        string="Billing Date",
        default=fields.Date.today
    )

    previous_reading = fields.Float(readonly=True)

    current_reading = fields.Float(readonly=True)

    usage = fields.Float(readonly=True)

    amount = fields.Float(
        string="Total Bill",
        readonly=True  
    )

    arrears = fields.Float(
    string="Arrears",
    readonly=True,
    default=0.0
    )


    payment_amount = fields.Float(
        string="Payment Amount",
        store=True
    )

    state = fields.Selection([
    ('unpaid', 'Unpaid'),
    ('paid', 'Paid'),
], string="Status", default='unpaid', readonly=True)


    payment_date = fields.Date(
        string="Payment Date",
        readonly=True
    )


    def action_pay_bill(self):
        for rec in self:
            if rec.state == 'paid':
                raise ValidationError("This bill is already paid.")

            if rec.payment_amount <= 0:
                raise ValidationError("Please enter a valid payment amount.")

            # Calculate arrears if payment is insufficient
            arrears = max(0.0, rec.amount - rec.payment_amount)

            # Mark bill as paid
            rec.write({
                'arrears': arrears,
                'state': 'paid',
                'payment_date': fields.Date.today(),
            })

            # Record payment history
            self.env['payment.history'].create({
                'transaction_id': rec.transaction_id,
                'reading_id': rec.reading_id.id,
                'reading_code': rec.reading_code,
                'member_id': rec.member_id.id,
                'billing_date': rec.billing_date,
                'previous_reading': rec.previous_reading,
                'current_reading': rec.current_reading,
                'usage': rec.usage,
                'amount': rec.amount,
                'payment_amount': rec.payment_amount,
                'arrears': arrears,
                'payment_date': fields.Date.today(),
                'state': 'paid',
            })

    def write(self, vals):
        for rec in self:
            if rec.state == 'paid':
                raise ValidationError("Paid bills cannot be modified.")
        return super().write(vals)

