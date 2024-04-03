from odoo import models, fields, api


class employee_contract(models.Model):
    _inherit = 'hr.employee'

    contract_ids = fields.One2many('hop.dong', 'id', string='contract_ids')

    status = fields.Selection([
        ('draft', 'Draft'),
        ('waiting_approve', 'Waiting Approve'),
        ('approved', 'Approved'),
        ('terminated', 'Terminated')],
        string='Status', default='draft')

    work_experience_ids = fields.One2many('employee.work.exp', 'employee_id')

    def action_draft(self):
        self.status = 'draft'

    def action_waiting_approve(self):
        self.status = 'waiting_approve'

    def action_approved(self):
        self.status = 'approved'

    def action_terminated(self):
        self.status = 'terminated'

    @api.multi
    def action_open_employee_contract(self):
        action = self.env.ref('test_module.action_hop_dong').read()[0]
        action['domain'] = [('employee_id', '=', self.id)]
        return action


