# -*- coding: utf-8 -*-
from odoo import models, fields, api
from datetime import date,datetime
from dateutil.relativedelta import relativedelta
from odoo.exceptions import ValidationError

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
    gross_salary = fields.Float(string='Lương gross', groups='payslip.group_hr_manager')
    net_salary = fields.Float(string='Lương net', groups='payslip.group_hr_manager')
    state = fields.Selection([
        ('new', 'New'),
        ('wait_payment', 'Wait payment'),
        ('paid', 'Paid'),
        ('close', 'Close')],
        string='Trạng thái', default='new')
    employee_id = fields.Many2one('hr.employee', string='Nhân viên')

    role_id = fields.Many2one('hr.role', string='Role')
    job_id = fields.Many2one('hr.job', string='Job')
    level_id = fields.Many2one('hr.level', string='Level')

    @api.onchange('employee_id')
    def _onchange_employee_id(self):
        if self.employee_id:
            # Tự động điền thông tin role, job, level khi chọn nhân viên
            self.role_id = self.employee_id.role_id
            self.job_id = self.employee_id.job_id
            self.level_id = self.employee_id.level_id

    @api.constrains('employee_id')
    def _check_employee_id(self):
        if not self.employee_id:
            raise ValidationError("Employee field cannot be empty.")

    @api.model
    def default_get(self, fields_list):
        defaults = super(Payslip, self).default_get(fields_list)
        if self._context.get('employee_id'):
            employee = self.env['hr.employee'].browse(self._context['employee_id'])
            defaults['onboard_date'] = employee.onboard_date
        return defaults
