# -*- coding: utf-8 -*-
from odoo import models, fields, api


class MyEmployee(models.Model):
    _inherit = 'hr.employee'

    payslip_ids = fields.One2many('hr.payslip', 'employee_id', string='Phiếu lương')

    status = fields.Selection([
        ('draft', 'Draft'),
        ('waiting_approve', 'Waiting Approve'),
        ('approved', 'Approved'),
        ('terminated', 'Terminated')],
        string='Status', default='draft')
    date_onboard = fields.Date(string='Date Onboard', readonly=True)
    date_terminated = fields.Date(string='Date Terminated', readonly=True)

    role_id = fields.Many2one('hr.role', string='Role')
    level_id = fields.Many2one('hr.level', string='Level')
    job_id = fields.Many2one('hr.job', string='Job')

    # @api.multi
    def action_view_payslips(self):
        action = self.env.ref('payslip.action_payslip').read()[0]
        action['domain'] = [('employee_id', '=', self.id)]
        return action

    # Action button Submit
    def action_submit(self):
        for employee in self:
            if employee.status == 'draft':
                employee.status = 'waiting_approve'

    # Action button Approve
    def action_approve(self):
        for employee in self:
            if employee.status == 'waiting_approve':
                employee.status = 'approved'

    # Action button Terminate
    def action_terminate(self):
        for employee in self:
            if employee.status == 'approved':
                employee.status = 'terminated'

    # Action button Set to Draft
    def action_set_to_draft(self):
        for employee in self:
            if employee.status == 'terminated':
                employee.status = 'draft'
