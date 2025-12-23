from odoo import models, fields, api

class WaterMember(models.Model):
    _name = "water.member"
    _description = "Water Member"
    _rec_name = "full_name"

    # member_id = fields.Char(string="Member ID", required=True)

    member_id = fields.Char(
    string="Customer ID",
    required=True,
    readonly=True,
    default=lambda self: self.env['ir.sequence'].next_by_code('water.member')
)


    first_name = fields.Char("First Name", required=True)
    middle_name = fields.Char("Middle Name")
    last_name = fields.Char("Last Name", required=True)

    partner_id = fields.Many2one(
        'res.partner',
        string="Customer",
        required=True,
        ondelete='restrict'
    )

    full_name = fields.Char(
            string="Full Name",
            compute="_compute_full_name",
            store=True
        )

    meter_number = fields.Char(string="Meter Number", required=True)
    address = fields.Text(string="Address")
    phone = fields.Char(string="Phone")


    @api.depends('first_name', 'middle_name', 'last_name')
    def _compute_full_name(self):   
        for rec in self:
            rec.full_name = " ".join(filter(None, [
                rec.first_name,
                rec.middle_name,
                rec.last_name
            ]))

    @api.model
    def create(self, vals):
        full_name = " ".join(filter(None, [
            vals.get('first_name'),
            vals.get('middle_name'),
            vals.get('last_name'),
        ]))
        
        partner = self.env['res.partner'].create({
            'name': full_name,
            'first_name': vals.get('first_name'),
            'last_name': vals.get('last_name'),
            'phone': vals.get('phone'),
            'street': vals.get('address'),
            'customer_rank': 1,
            'is_company': False,
        })

        vals['partner_id'] = partner.id
        return super().create(vals)