
from odoo import models, fields

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

    livestock_total_amount = fields.Float(string="Price/Kilo")



