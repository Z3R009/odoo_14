from odoo.exceptions import ValidationError
from odoo import models, fields, api

class ResPartner(models.Model):
    _inherit = 'res.partner'

    first_name = fields.Char("First Name")
    middle_name = fields.Char("Middle Name")
    last_name = fields.Char("Last Name")
    is_water_member = fields.Boolean("For Water Billing")
    member_id = fields.Char("Customer ID", readonly=True, store=True, ondelete='cascade', copy=False,
        default=lambda self: self.env['ir.sequence'].next_by_code('water.member'))


    @api.onchange('first_name', 'middle_name', 'last_name')
    def _onchange_name_parts(self):
        self.name = ' '.join(filter(None, [
            self.first_name,
            self.middle_name,
            self.last_name
        ]))

    @api.model
    def create(self, vals):
        if not vals.get('name'):
            vals['name'] = ' '.join(filter(None, [
                vals.get('first_name'),
                vals.get('middle_name'),
                vals.get('last_name')
            ]))
        return super().create(vals)

    def write(self, vals):
        if any(k in vals for k in ('first_name', 'middle_name', 'last_name')):
            vals['name'] = ' '.join(filter(None, [
                vals.get('first_name', self.first_name),
                vals.get('middle_name', self.middle_name),
                vals.get('last_name', self.last_name)
            ]))
        return super().write(vals)
    
    @api.onchange('is_company')
    def _onchange_is_company(self):
        if self.is_company:
            self.first_name = False
            self.middle_name = False
            self.last_name = False

    @api.constrains('is_company', 'first_name', 'last_name')
    def _check_name_integrity(self):
            for partner in self:
                if not partner.is_company:
                    if not partner.first_name or not partner.last_name:
                        raise ValidationError(
                            "Individual contacts must have a first and last name."
                        )

