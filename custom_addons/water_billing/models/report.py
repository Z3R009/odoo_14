from odoo import models, api, fields

class ReportWaterBilling(models.AbstractModel):
    _name = 'report.water_billing.report_water_billing'
    _description = 'Water Billing Report'

    @api.model
    def _get_report_values(self, docids, data=None):
        docs = self.env['water.billing'].browse(docids)
        total_amount = sum(doc.amount or 0 for doc in docs)

        # Generate filename: WaterBilling-YYYY-MM-DD
        today_str = fields.Date.context_today(self).strftime('%Y-%m-%d')
        file_name = f"WaterBilling-{today_str}" 

        return {
            'doc_ids': docids,
            'doc_model': 'water.billing',
            'docs': docs,
            'total_amount': total_amount,
            'report_name': file_name, 
        }
