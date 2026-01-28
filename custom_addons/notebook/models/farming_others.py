
from odoo import models, fields

class FarmingOthers(models.Model):
    _name = 'farming.others'
    _description = 'Farming Others'

    farming_form_id = fields.Many2one('form.model', string='Form', required=True)  
    

    farming_others = fields.Char(string='Others', required=True ) 

    farm_location_o = fields.Char(string="Farm Area Location")

    income = fields.Float(string="Income")

    total_harvest_per_year = fields.Float(string="Total Harvest per Year")

    avg_monthly_prod_o = fields.Float(string="Average Monthly Production")

    others_total_amount = fields.Float(string="Total Amount")



