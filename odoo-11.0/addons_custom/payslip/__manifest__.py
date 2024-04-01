{
    'name': 'Quản lý Phiếu Lương',
    'version': '1.0',
    'summary': 'Quản lý thông tin phiếu lương nhân viên',
    'description': """
        Module này cho phép quản lý thông tin về các phiếu lương của nhân viên.
    """,
    'author': 'Dattc',
    'depends': ['base', 'hr'],
    'data': [
        'views/hr_payslip_views.xml',
        'data/payslip_sequenxe_data.xml',
        'data/button_display_payslip.xml',
        'data/hr_job_form_inherit.xml',
        'data/filter_employee.xml',
        'data/display_extra_data.xml',
    ],
    'installable': True,
    'application': True,
}
