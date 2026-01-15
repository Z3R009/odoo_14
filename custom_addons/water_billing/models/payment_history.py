from odoo import models, fields
from odoo.exceptions import ValidationError

class PaymentHistory(models.Model):
    _name = "payment.history"
    _description = "Payment History"
    _order = "payment_date desc, id desc"

    transaction_id = fields.Char(
        # 'pay.bills',
        string="Transaction ID"
        )
    
    pay_bill_id = fields.Many2one(
        'pay.bills',
        string="Bill",
        ondelete='cascade'
    )
    reading_id = fields.Many2one('read.meter', string="Reading ID")
    reading_code = fields.Char(string="Reading ID")
    member_id = fields.Many2one('res.partner', string="Customer Name", ondelete='cascade')
    billing_date = fields.Datetime(string="Billing Date")
    previous_reading = fields.Float()
    current_reading = fields.Float()
    usage = fields.Float()
    
    start_date = fields.Date(
        string="Start Date",
        readonly=True
    )

    end_date = fields.Date(
        string="End Date",
        readonly=True
    )

    billing_month = fields.Char(
        string="Billing Month",
        readonly=True
    )


    current_charges = fields.Float(string="Current Charges")
    amount = fields.Float(string="Total Bill")
    payment_amount = fields.Float(string="Amount Paid", store=True)
    change = fields.Float(string="Change", store=True)
    arrears = fields.Float(string="Arrears", store=True)
    payment_date = fields.Date(string="Payment Date")
    state = fields.Selection(
        related='pay_bill_id.state',
        string="Status",
        readonly=True
    )