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
    job_id = fields.Many2one('employee.job', string='Jobs')
    level_id = fields.Many2one('employee.level', string='Levels')
    role_id = fields.Many2one('employee.role', string='Roles')
    reference = fields.Char(string='Reference')

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

    @api.constrains('job_id', 'level_id', 'role_id')
    def _check_unique_work_exp(self):
        if not self._check_date():
            for record in self:
                if self.search_count([
                    ('role_id', '=', record.role_id.id),
                    ('job_id', '=', record.job_id.id),
                    ('level_id', '=', record.level_id.id),
                    ('employee_id', '=', record.employee_id.id),
                    ('id', '!=', record.id)
                ]):
                    raise ValidationError(_('Role Job Level combination must be unique!'))