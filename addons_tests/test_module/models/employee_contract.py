from odoo import models, fields, api


class employee_contract(models.Model):
    _inherit = 'hr.employee'

    contract_ids = fields.One2many('hop.dong', 'id', string='contract_ids')

    @api.multi
    def action_open_employee_contract(self):
        action = self.env.ref('test_module.action_hop_dong').read()[0]
        action['domain'] = [('employee_id', '=', self.id)]
        return action
