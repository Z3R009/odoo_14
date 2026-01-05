from odoo import models, fields, api
from odoo.exceptions import ValidationError, UserError
from datetime import datetime

class ReadMeter(models.Model):
    _name = "read.meter"
    _description = "Read Meter"

    reading_id = fields.Char(
        string="Reading ID",
        required=True,
        readonly=True,
        store=True,
        default=lambda self: self.env['ir.sequence'].next_by_code('read.meter')
    )   

    billing_date = fields.Date(
        string="Billing Date",
        default=fields.Date.today
    )

    billing_time = fields.Datetime(
        string="Billing Time",
        default=lambda self: fields.Datetime.now()
    )

    billing_datetime = fields.Datetime(
        string="Billing Date & Time",
        compute="_compute_billing_datetime",
        store=True
    )

    member_id = fields.Many2one(
        'res.partner',
        string="Customer",
        required=True,
        domain="[('is_water_member','=',True)]",
        ondelete='cascade'
    )

    previous_reading = fields.Float(string="Previous Reading")

    current_reading = fields.Float(
    string="Current Reading",
    compute="_compute_current_reading",
    store=True
)

    usage = fields.Float(string="Usage")
    
    amount = fields.Float(
    string="Total Amount",
    compute="_compute_amount",
    store=True
)

    arrears = fields.Float(
        string="Arrears",
        readonly=True,
        store=True,
        default=0.0,
        help="Any unpaid amount from previous bills"
    )

    @api.depends('usage', 'arrears')
    def _compute_amount(self):
        for rec in self:
            rec.amount = (rec.usage or 0) * 15 + (rec.arrears or 0)

    @api.depends('previous_reading', 'usage')
    def _compute_current_reading(self):
        for rec in self:
            rec.current_reading = (rec.previous_reading or 0) + (rec.usage or 0)


    @api.depends('billing_date', 'billing_time')
    def _compute_billing_datetime(self):
        for rec in self:
            if rec.billing_date and rec.billing_time:
                rec.billing_datetime = datetime.combine(
                    rec.billing_date, rec.billing_time.time()
                )
            else:
                rec.billing_datetime = False

    @api.model
    def create(self, vals):
        """Set previous reading and include arrears from latest bill"""
        if 'member_id' in vals:  
            # Previous reading
            last_billing = self.search(
                [('member_id', '=', vals['member_id'])],
                order='billing_date desc, id desc',
                limit=1
            )
            vals['previous_reading'] = last_billing.current_reading if last_billing else 0

            # Latest pay.bills record
            latest_bill = self.env['pay.bills'].search(
                [('member_id', '=', vals['member_id'])],
                order='billing_date desc, id desc',
                limit=1
            )
            vals['arrears'] = latest_bill.arrears if latest_bill and latest_bill.arrears > 0 else 0.0

        # Current reading
        if 'usage' in vals:
            vals['current_reading'] = vals['previous_reading'] + vals['usage']

        rec = super(ReadMeter, self).create(vals)

        # Create pay.bills with arrears included
        self.env['pay.bills'].create({
            'reading_id': rec.id,
            'member_id': rec.member_id.id,
            'billing_date': rec.billing_date,
            'previous_reading': rec.previous_reading,
            'current_reading': rec.current_reading,
            'usage': rec.usage,
            # 'amount': rec.amount + rec.arrears,
            'amount': rec.amount,
            'arrears': rec.arrears,
            'paid': False,
        })

        return rec


    @api.onchange('member_id')
    def _onchange_member_id(self):
        """Fill previous reading and arrears from latest bill"""
        if not self.member_id:
            self.previous_reading = 0
            self.arrears = 0.0
            return

        # Get last read.meter record for previous reading
        last_billing = self.env['read.meter'].search(
            [('member_id', '=', self.member_id.id)],
            order='billing_date desc, id desc',
            limit=1
        )
        self.previous_reading = last_billing.current_reading if last_billing else 0

        # Get the latest pay.bills record for this member
        latest_bill = self.env['pay.bills'].search(
            [('member_id', '=', self.member_id.id)],
            order='billing_date desc, id desc',
            limit=1
        )
        self.arrears = latest_bill.arrears if latest_bill and latest_bill.arrears > 0 else 0.0



    # @api.onchange('usage')
    # def _onchange_usage(self):
    #     """Calculate current reading based on usage"""
    #     for rec in self:
    #         rec.current_reading = rec.previous_reading + rec.usage if rec.usage else rec.previous_reading

    def action_pay(self):
        """Simple pay action - optional"""
        for record in self:
            if hasattr(record, 'payment_amount') and record.payment_amount < record.amount:
                raise ValidationError(
                    f"Payment amount ({record.payment_amount}) is less than the billed amount ({record.amount})!"
                )
            record.paid = True

    def action_generate_report(self):
        """Generate PDF report of billing records"""
        records = self.search([])
        if not records:
            raise UserError("No billing records found to generate a report.")
        return self.env.ref('water_billing.action_water_billing_report').report_action(records)
  