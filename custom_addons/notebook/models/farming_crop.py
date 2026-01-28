
from odoo import api, models, fields

class FarmingCrop(models.Model):
    _name = 'farming.crop.model'
    _description = 'Farming Crop'

    farming_form_id = fields.Many2one('form.model', string='Form', required=True)  
    


    # crop section

    farming_crop_type = fields.Selection([
        ('corn', 'Corn'),
        ('rice', 'Rice'),
        ('fruit_trees', 'Fruit Trees'),
        ('vegetables', 'Vegetables'),
        ('banana', 'Banana'),
    ], string='Crop', required=True ) 

    crop_farm_location = fields.Char(string="Farm Area Location")

    volume = fields.Integer(string="Volume")

    kg_per_sack = fields.Float(string="Kg per Sack")

    crop_price = fields.Float(string="Price/Kilo")

    crop_months_to_harvest = fields.Float(string="Months to Harvest")

    crop_avg_monthly_prod = fields.Float(string="Average Monthly Production")

    crop_total_amount = fields.Float(
        string="Total Amount",
        compute='_compute_total_amount',
        store=True)


    @api.depends('volume', 'kg_per_sack', 'crop_price')
    def _compute_total_amount(self):
        for record in self:
            if record.volume and record.kg_per_sack and record.crop_price:
                record.crop_total_amount = (
                    record.volume
                    * record.kg_per_sack
                    * record.crop_price
                )
            else:
                record.crop_total_amount = 0




