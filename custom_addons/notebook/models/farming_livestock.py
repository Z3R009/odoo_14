
from odoo import models, fields, api

class FarmingLivestock(models.Model):
    _name = 'farming.livestock.model'
    _description = 'Farming Livestock'

    farming_form_id = fields.Many2one('form.model', string='Form', required=True)  

    # livestock section

    farming_livestock_type = fields.Selection([
        ('piggery', 'Piggery'), 
        ('poultry', 'Poultry'), 
        ('fish_pond', 'Fish Pond'), 
        ('layer', 'Layer (eggs)'), 
    ], string='Livestock', required=True )

    livestock_farm_location = fields.Char(string="Farm Area Location")

    livestock_weight_per_head = fields.Integer(string="Weight per Head (in Kgs)")

    livestock_no_of_heads = fields.Float(string="Number of Heads")

    livestock_price = fields.Float(string="Price/Kilo")

    livestock_months_to_harvest = fields.Float(string="Months to Harvest")

    livestock_avg_monthly_prod = fields.Float(string="Average Monthly Production")

    livestock_total_amount = fields.Float(
        string="Total Amount",
        compute='_compute_livestock_total_amount',
        store=True)



    @api.depends('livestock_no_of_heads', 'livestock_weight_per_head', 'livestock_price', 'livestock_months_to_harvest')
    def _compute_livestock_total_amount(self):
        for record in self:
            if record.livestock_months_to_harvest:  # avoid division by zero
                record.livestock_total_amount = (
                    (record.livestock_no_of_heads or 0)
                    * (record.livestock_weight_per_head or 0)
                    * (record.livestock_price or 0)
                    / record.livestock_months_to_harvest
                )
            else:
                record.livestock_total_amount = 0

