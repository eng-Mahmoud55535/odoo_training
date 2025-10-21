
from odoo import models, fields

class CrmLead(models.Model):
    _inherit = 'crm.lead'

    crm_lead_user_id = fields.Many2one(
        'res.users',
        string='CRM Lead User',
        default=lambda self: self.env.user,
    )
       lead_visibility = fields.Selection([
          ('user', 'User'),
          ('admin', 'Admin'),
       ], string='Visibility', default='user')

      @api.model
      def default_get(self, fields_list):
          res = super().default_get(fields_list)
          if self.env.user.has_group('base.group_system'):
              res['lead_visibility'] = 'admin'
          else:
              res['lead_visibility'] = 'user'
          return res
