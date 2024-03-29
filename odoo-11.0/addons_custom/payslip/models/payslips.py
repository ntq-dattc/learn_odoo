# -*- coding: utf-8 -*-
from odoo import models, fields, api
from datetime import date,datetime
from dateutil.relativedelta import relativedelta

class Payslip(models.Model):
    _name = 'hr.payslip'
    _description = 'Payslip'

    name = fields.Char('Tên',  default='New')

    @api.model
    def create(self, vals):
        if vals.get('name', 'New') == 'New':
            vals['name'] = self.env['ir.sequence'].next_by_code('hr.payslip.name')

        result = super(Payslip, self).create(vals)

        return result

    start_date = fields.Date(string='Ngày bắt đầu', default=lambda self: date.today().replace(day=1))
    end_date = fields.Date(string='Ngày kết thúc', default=lambda self: (datetime.now() + relativedelta(day=31)).date())
    actual_working_hours = fields.Float(string='Số giờ làm việc thực tế')
    standard_working_hours = fields.Float(string='Số giờ công tiêu chuẩn')
    gross_salary = fields.Float(string='Lương gross')
    net_salary = fields.Float(string='Lương net')
    state = fields.Selection([
        ('new', 'New'),
        ('wait payment', 'Wait payment'),
        ('paid', 'Paid'),
        ('close', 'Close')],
        string='Trạng thái', default='new')
    employee_id = fields.Many2one('hr.employee', string='Nhân viên')