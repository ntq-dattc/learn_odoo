from odoo import *
from odoo import _
from odoo.exceptions import ValidationError, AccessError


class work_exp(models.Model):
    _name = 'employee.work.exp'
    _description = 'employee work exp'

    employee_id = fields.Many2one('hr.employee', string='Employee')
    from_date = fields.Date(string='From ', format='%Y-%m-%d', required=True)
    to_date = fields.Date(string='To ', format='%Y-%m-%d', required=True)
    company = fields.Char(string='Company ', required=True)
    job_ids = fields.Many2one('employee.job', string='Jobs')
    level_ids = fields.Many2one('employee.level', string='Levels')
    role_ids = fields.Many2one('employee.role', string='Roles')
    reference = fields.Char(string='Reference')

    manager_id = fields.Many2one('hr.employee')

    def _check_date(self):
        for record in self:
            if not record.from_date or not record.to_date:
                continue

            domain = [
                ('from_date', '<=', record.from_date),
                ('to_date', '>=', record.to_date)
            ]

            if record.env['employee.work.exp'].search_count(domain) > 0:
                return False

        return True

    @api.constrains('from_date', 'to_date')
    def _check_validate_date(self):
        if self.to_date < self.from_date:
            raise ValidationError(_('From date must be before to date!'))

    @api.constrains('job_ids', 'level_ids', 'role_ids')
    def _check_unique_work_exp(self):
        for record in self:
            if self.search_count([
                ('role_ids', '=', record.role_ids.id),
                ('job_ids', '=', record.job_ids.id),
                ('level_ids', '=', record.level_ids.id),
                ('employee_id', '=', record.employee_id.id),
                ('id', '!=', record.id)
            ]):
                raise ValidationError(_('Role Job Level combination must be unique!'))

    @api.constrains('from_date')
    def _check_manager_edit_permission(self):
        for employee in self:
            if employee.manager_id != self.env.user.employee_ids:
                raise ValidationError("Only the employee's manager can edit the employee's information.")