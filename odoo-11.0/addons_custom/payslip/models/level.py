from odoo import models, fields

class Level(models.Model):
    _name = 'hr.level'
    name = fields.Char(string='Level Name')
    code = fields.Char(string='Level Code')
