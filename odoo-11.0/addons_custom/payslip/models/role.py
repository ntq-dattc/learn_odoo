from odoo import models, fields

class Role(models.Model):
    _name = 'hr.role'
    name = fields.Char(string='Role Name')
    code = fields.Char(string='Role Code')
