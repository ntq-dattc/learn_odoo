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

    history_employee_ids = fields.One2many('employee.history', 'employee_id', string='History Employees')

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

    @api.model
    def name_search(self, name='', args=None, operator='ilike', limit=100):
        if self._context.get('custom_employee_name_search'):
            return self.env['hr.employee'].custom_payslip_name_search(name=name, args=args, operator=operator,
                                                                      limit=limit)
        else:
            return super(MyEmployee, self).name_search(name=name, args=args, operator=operator, limit=limit)

    @api.model
    def custom_payslip_name_search(self, name='', args=None, operator='ilike', limit=100):
        domain = [('name', operator, name), ('status', '=', 'approved')]
        employees = self.search(domain, limit=limit)
        return employees.name_get()
