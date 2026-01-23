
from odoo import models, fields

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

    crop_weight_per_head = fields.Integer(string="Weight per Head (in Kgs)")

    crop_no_of_heads = fields.Float(string="Number of Heads")

    crop_price = fields.Float(string="Price/Kilo")

    crop_months_to_harvest = fields.Float(string="Months to Harvest")

    crop_avg_monthly_prod = fields.Float(string="Average Monthly Production")

    crop_total_amount = fields.Float(string="Price/Kilo")




