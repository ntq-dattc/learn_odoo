from odoo import models, fields

class Job(models.Model):
    _inherit = 'hr.job'
    name = fields.Char(string='Job Name')
    code = fields.Char(string='Job Code')
