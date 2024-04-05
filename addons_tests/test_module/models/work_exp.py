from odoo import models, fields, api


class work_exp(models.Model):
    _name = 'employee.work.exp'
    _description = 'employee work exp'

    employee_id = fields.Many2one('hr.employee', string='Employee')
    from_date = fields.Date(string='From ', format='%Y-%m-%d', required=True)
    to_date = fields.Date(string='To ', format='%Y-%m-%d', required=True)
    company = fields.Char(string='Company ', required=True)
    job_ids = fields.One2many('employee.job', 'work_exp_id', string='Jobs')
    level_ids = fields.One2many('employee.level', 'work_exp_id', string='Levels')
    role_ids = fields.One2many('employee.role', 'work_exp_id', string='Roles')
    reference = fields.Char(string='Reference')

    job_names = fields.Char(string='Job Names', related='job_ids.name', store=True)
    level_names = fields.Char(string='Level Names', related='level_ids.name', store=True)
    role_names = fields.Char(string='Role Names', related='role_ids.name', store=True)