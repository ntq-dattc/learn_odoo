from odoo import models, fields, api


class job(models.Model):
    _name = 'employee.job'
    _description = 'employee job'

    name = fields.Char(string='Job')
    code = fields.Char(string='Job Code')
