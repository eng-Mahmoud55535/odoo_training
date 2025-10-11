from odoo import models, fields

class ProjectLeadWizard(models.TransientModel):
    _name = 'project.lead.wizard'
    _description = 'Wizard to create CRM Lead'

    name = fields.Char(string='Lead Name', required=True)

    def create_lead(self):
        self.env['crm.lead'].create({'name': self.name})

