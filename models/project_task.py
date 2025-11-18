from odoo import models, fields, api

class ProjectTask(models.Model):
    _inherit = 'project.task'

    project_days = fields.Integer(string='Project Days', default=0)
    project_user_id = fields.Many2one('res.users', string='Project User')
    project_actual_days = fields.Integer(string='Project Actual Days', compute='_compute_actual_days', store=True)

    @api.depends('planned_start_date', 'planned_end_date')
    def _compute_actual_days(self):
        for rec in self:
            if rec.planned_start_date and rec.planned_end_date:
                rec.project_actual_days = (rec.planned_end_date - rec.planned_start_date).days
            else:
                rec.project_actual_days = 0

