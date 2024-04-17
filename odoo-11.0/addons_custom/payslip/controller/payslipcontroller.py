# -*- coding: utf-8 -*-
from odoo import http
from odoo.http import request


class PayslipController(http.Controller):

    @http.route('/payslip/view', auth='none', type='http')
    def view_payslip(self, **kwargs):
        # Lấy danh sách các bản ghi từ bảng payslip
        payslips = request.env['hr.payslip'].sudo().search([])

        # Trả về view payslip với danh sách các bản ghi payslip
        return http.request.render('payslip.report_payslip_template_test', {'docs': payslips})
