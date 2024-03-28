from odoo import models, fields


class hop_dong(models.Model):
    _name = 'hop.dong'
    _description = 'hop dong'

    name = fields.Char(string='ten')
    start_date = fields.Datetime(string='ngay bat dau')
    end_date = fields.Datetime(string='ngay ket thuc')
    contract_type = fields.Char(string='loai hop dong')
    signed_date = fields.Datetime(string='ngay ky')
    salary_rack = fields.Float(string='luong ngach bac')
    efficiency_wage = fields.Float(string='luong hieu qua')
    status = fields.Selection([
        ('draft', 'ban nhap'),
        ('ongoing', 'dang dien ra'),
        ('expired', 'het han')],
        string='trang thai', default='draft')
