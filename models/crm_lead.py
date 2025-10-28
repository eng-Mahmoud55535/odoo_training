<<<<<<< HEAD

from odoo import models, fields
=======
from odoo import fields, models, api
>>>>>>> c44e047 (task report and wizard)

class CrmLead(models.Model):
    _inherit = 'crm.lead'

<<<<<<< HEAD
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
=======
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

    @api.model
    def _default_crm_lead_user(self):
        user_id = self.env.user.id
        if user_id == 3:
            demo_user = self.env.ref('base.user_demo', raise_if_not_found=False)
            return demo_user.id if demo_user else user_id
        return user_id

class ResUsers(models.Model):
    _inherit = 'res.users'
    pass
>>>>>>> c44e047 (task report and wizard)
