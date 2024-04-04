from odoo import models, fields, api


class level(models.Model):
    _name = 'employee.level'
    _description = 'employee level'

    name = fields.Char(string='Level')
    code = fields.Char(string='Level Code')
    work_exp_id = fields.Many2one('employee.work.exp')
