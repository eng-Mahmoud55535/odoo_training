
from odoo import fields, models, api

class CrmLead(models.Model):
    _inherit = 'crm.lead'

    x_crm_lead_user_id = fields.Many2one(
        'res.users',
        string='CRM Lead User',
        default=lambda self: self._default_crm_lead_user(),
    )

    x_crm_lead_user_display = fields.Char(
        string='CRM Lead User Display',
        compute='_compute_crm_lead_user_display',
        store=False,
    )

    def _compute_crm_lead_user_display(self):
        is_admin = self.env.user.has_group('base.group_erp_manager') or self.env.user.has_group('base.group_system')
        for record in self:
            if is_admin:
                record.x_crm_lead_user_display = "Admin"
            else:
                record.x_crm_lead_user_display = "User"
