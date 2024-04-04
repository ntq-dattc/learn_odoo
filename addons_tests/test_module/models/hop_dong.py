from odoo import models, fields, api
from datetime import *


def get_signed_date():
    signed_date = datetime.now() + timedelta(weeks=1)
    if signed_date.weekday() == 5:
        signed_date += timedelta(days=2)
    elif signed_date.weekday() == 6:
        signed_date += timedelta(days=1)
    return signed_date


class hop_dong(models.Model):
    _name = 'hop.dong'
    _description = 'hop dong'

    name = fields.Char(string='Name')
    start_date = fields.Datetime(string='Start Date: ', default=fields.Datetime.now, format='%Y-%m-%d')
    end_date = fields.Datetime(string='End Date: ')
    contract_type = fields.Char(string='Contract Type: ')
    signed_date = fields.Datetime(string='Signed Date: ', default=get_signed_date())
    salary_rack = fields.Float(string='Standard Salary: ')
    efficiency_wage = fields.Float(string='Efficiency Wage: ')
    status = fields.Selection([
        ('new', 'New'),
        ('running', 'Running'),
        ('expired', 'Expired'),
        ('pause', 'Pause')],
        string='Status', default='new')

    employee_id = fields.Many2one('hr.employee', string='Employee')

    employee_name = fields.Char(string='Employee Name', required=True, compute='_compute_employee_name')

    total_salary = fields.Float(string='Total Salary', compute='_compute_total_salary')

    @api.depends('salary_rack', 'efficiency_wage')
    def _compute_total_salary(self):
        for record in self:
            record.total_salary = record.salary_rack + record.efficiency_wage

    @api.depends('employee_id')
    def _compute_employee_name(self):
        for record in self:
            record.employee_name = record.employee_id.name
