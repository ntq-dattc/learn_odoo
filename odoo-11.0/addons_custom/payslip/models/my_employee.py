# -*- coding: utf-8 -*-
from odoo import models, fields, api


class MyEmployee(models.Model):
    _inherit = 'hr.employee'

    payslip_ids = fields.One2many('hr.payslip', 'employee_id', string='Phiếu lương')

    # @api.multi
    def action_view_payslips(self):
        action = self.env.ref('payslip.action_payslip').read()[0]
        action['domain'] = [('employee_id', '=', self.id)]
        return action
