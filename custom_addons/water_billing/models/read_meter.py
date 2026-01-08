from odoo import models, fields, api
from odoo.exceptions import ValidationError, UserError
from datetime import datetime
from datetime import timedelta

class ReadMeter(models.Model):
    _name = "read.meter"
    _description = "Read Meter"
    _order = "billing_date desc, id desc"

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

    due_date = fields.Date(
    string="Due Date",
    compute="_compute_due_and_disconnect",
    store=True
)

    disconnection_date = fields.Date(
        string="Disconnection Date",
        compute="_compute_due_and_disconnect",
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

    current_charges = fields.Float(
        string="Current Charges",
        compute="_compute_charges",
        store=True
    )
    
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

    state = fields.Selection([
        ('draft', 'Draft'),
        ('confirmed', 'Confirmed')
    ], string="Status", default='draft', readonly=True, store=True)

    @api.depends('usage', 'current_charges')
    def _compute_charges(self):
        for rec in self:
            rec.current_charges = (rec.usage or 0) * 15

            

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

    
#   due date and disconnection date
    @api.depends('billing_date')
    def _compute_due_and_disconnect(self):
        for rec in self:
            if rec.billing_date:
                rec.due_date = rec.billing_date + timedelta(days=15)
                rec.disconnection_date = rec.due_date + timedelta(days=3)
            else:
                rec.due_date = False
                rec.disconnection_date = False

    @api.model
    def create(self, vals):
        """Set previous reading and arrears from latest bill, 
        prevent creating new reading if a draft exists,
        and prevent creating new reading if the latest bill is unpaid."""
        
        if 'member_id' in vals:
            member_id = vals['member_id']

            # Check for existing draft for this customer
            existing_draft = self.search([
                ('member_id', '=', member_id),
                ('state', '=', 'draft')
            ], limit=1)
            if existing_draft:
                raise ValidationError(
                    "There is already a draft billing for this customer. "
                    "Please confirm it before creating a new reading."
                )

            # Check for unpaid bills
            unpaid_bill = self.env['pay.bills'].search([
                ('member_id', '=', member_id),
                ('state', '!=', 'paid')  # assuming 'paid' is the state for paid bills
            ], limit=1)
            if unpaid_bill:
                raise ValidationError(
                    "The customer has unpaid bills. Please settle the previous bill before creating a new reading."
                )

            # Previous reading
            last_billing = self.search(
                [('member_id', '=', member_id)],
                order='billing_date desc, id desc',
                limit=1
            )
            vals['previous_reading'] = last_billing.current_reading if last_billing else 0

            # Latest pay.bills record for arrears
            latest_bill = self.env['pay.bills'].search(
                [('member_id', '=', member_id)],
                order='billing_date desc, id desc',
                limit=1
            )
            vals['arrears'] = latest_bill.arrears if latest_bill and latest_bill.arrears > 0 else 0.0

        # Current reading
        if 'usage' in vals:
            vals['current_reading'] = vals['previous_reading'] + vals['usage']

        rec = super(ReadMeter, self).create(vals)
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
  
# confirm button
    def write(self, vals):
            """Prevent editing confirmed records"""
            for rec in self:
                if rec.state == 'confirmed':
                    raise ValidationError("This record is confirmed and cannot be edited!")
            return super(ReadMeter, self).write(vals)

    def action_confirm(self):
        """Confirm the bill and create pay.bills record"""
        for rec in self:
            if rec.state != 'draft':
                continue
            # Change state
            rec.state = 'confirmed'

            # Create pay.bills record at confirmation
            self.env['pay.bills'].create({
                'reading_id': rec.id,
                'member_id': rec.member_id.id,
                'billing_date': rec.billing_date,
                'previous_reading': rec.previous_reading,
                'current_reading': rec.current_reading,
                'usage': rec.usage,
                'current_charges': rec.current_charges,
                'amount': rec.amount,
                'arrears': rec.arrears,
                'state': False,
            })
