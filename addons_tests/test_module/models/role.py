from odoo import models, fields, api


class role(models.Model):
    _name = 'employee.role'
    _description = 'employee role'

    name = fields.Char(string='Role',)
    code = fields.Char(string='Role Code')
    work_exp_id = fields.Many2one('employee.work.exp')