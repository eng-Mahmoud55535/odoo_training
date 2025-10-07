from odoo import models, fields, api
from odoo.exceptions import ValidationError

class ProjectSubtask(models.Model):
    _name = 'project.subtask'
    _description = 'Project Subtask'

    tags = fields.Char(string="Tags")
    project_days = fields.Integer(string="Project Days")

    @api.constrains('project_days')
    def _check_project_days(self):
        for rec in self:
            if rec.project_days <= 365:
                raise ValidationError("Project Days must be greater than 365.")
