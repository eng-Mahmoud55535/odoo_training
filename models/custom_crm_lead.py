from odoo import models, fields

class CrmLead(models.Model):
    _inherit = 'crm.lead'

    next_call_date = fields.Datetime(string='Next Call Date')

