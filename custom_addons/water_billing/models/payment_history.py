from odoo import models, fields
from odoo.exceptions import ValidationError

class PaymentHistory(models.Model):
    _name = "payment.history"
    _description = "Payment History"

    transaction_id = fields.Char(
        # 'pay.bills',
        string="Transaction ID"
        )
    reading_id = fields.Many2one('read.meter', string="Reading ID")
    reading_code = fields.Char(string="Reading ID")
    member_id = fields.Many2one('res.partner', string="Customer Name", ondelete='cascade')
    billing_date = fields.Datetime(string="Billing Date")
    previous_reading = fields.Float()
    current_reading = fields.Float()
    usage = fields.Float()
    amount = fields.Float(string="Total Bill")
    payment_amount = fields.Float(string="Amount Paid", store=True)
    arrears = fields.Float(string="Arrears", store=True)
    payment_date = fields.Date(string="Payment Date")
    state = fields.Boolean(default=True)