# -*- coding: utf-8 -*-
from odoo import models, fields

class Employee(models.Model):
    _name = 'hr.employee'

    payslip_ids = fields.One2many('hr.payslip', 'employee_id', string='Phiếu lương')
