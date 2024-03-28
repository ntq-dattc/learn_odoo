from mock.mock import self

from odoo import models, fields
import calendar
from datetime import *


def get_signed_date():
    signed_date =  datetime.now() + timedelta(weeks=1)
    if signed_date.weekday() == 5:
        signed_date += timedelta(days=2)
    elif signed_date.weekday() == 6:
        signed_date += timedelta(days=1)
    return signed_date


class hop_dong(models.Model):
    _name = 'hop.dong'
    _description = 'hop dong'

    def get_running_contracts(self):
        return

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
    running_contracts = fields.