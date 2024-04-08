from odoo import models, fields, api
from datetime import datetime
from dateutil.relativedelta import relativedelta

class EmployeeHistory(models.Model):
    _name = 'employee.history'
    _description = 'History Employee'

    employee_id = fields.Many2one('hr.employee', string='Employee')
    start = fields.Date(string='Start Date', required=True)
    end = fields.Date(string='End Date')
    role_id = fields.Many2one('hr.role', string='Role', required=True)
    job_id = fields.Many2one('hr.job', string='Job', required=True)
    level_id = fields.Many2one('hr.level', string='Level', required=True)
    create_at = fields.Datetime(string='Create At', default=lambda self: datetime.now(), readonly=True)
    update_at = fields.Datetime(string='Update At', default=lambda self: datetime.now(), readonly=True)
    time = fields.Float(string='Time (months)', compute='_compute_time', store=True)

    @api.depends('start', 'end')
    def _compute_time(self):
        for record in self:
            start_date = fields.Date.from_string(record.start)
            end_date = fields.Date.from_string(record.end) if record.end else datetime.now().date()
            duration = relativedelta(end_date, start_date)
            record.time = duration.years * 12 + duration.months

    @api.model
    def create(self, vals):
        last_record = self.search([('employee_id', '=', vals.get('employee_id')), ('end', '=', False)], order='start DESC', limit=1)
        if last_record:
            start_date = fields.Date.from_string(vals['start'])
            last_record.write({'end': fields.Date.to_string(start_date - relativedelta(days=1))})
        return super(EmployeeHistory, self).create(vals)
