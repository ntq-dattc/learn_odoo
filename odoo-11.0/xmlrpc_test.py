# -*- coding: utf-8 -*-
try:
    from xmlrpc import client as xmlrpclib
except:
    import xmlrpclib

# Kết nối tới server Odoo XML-RPC
url = 'http://d-os1-dattc2.ntq-solution.com.vn:8069'
db = 'dattc'
username = 'dattc'
password = '12345'

common = xmlrpclib.ServerProxy('{}/xmlrpc/2/common'.format(url))
uid = common.authenticate(db, username, password, {})

models = xmlrpclib.ServerProxy('{}/xmlrpc/2/object'.format(url))

# Hàm tạo mới một bản ghi Payslip
def create_payslip(data):
    payslip_id = models.execute_kw(db, uid, password, 'hr.payslip', 'create', [data])
    return payslip_id

# Hàm cập nhật một bản ghi Payslip
def update_payslip(payslip_id, data):
    models.execute_kw(db, uid, password, 'hr.payslip', 'write', [[payslip_id], data])
    return True

# Hàm xóa một bản ghi Payslip
def delete_payslip(payslip_id):
    models.execute_kw(db, uid, password, 'hr.payslip', 'unlink', [[payslip_id]])
    return True

# Hàm lấy danh sách tất cả bản ghi Payslip
def get_all_payslips():
    payslips = models.execute_kw(db, uid, password, 'hr.payslip', 'search_read', [[]], {
        'fields': ['name', 'start_date', 'end_date', 'actual_working_hours', 'standard_working_hours', 'gross_salary',
                   'net_salary', 'state', 'employee_id', 'role_id', 'job_id', 'level_id']})

    for payslip in payslips:  # Duyệt qua từng bản ghi trong danh sách payslips
        payslip['employee_id'] = {'id': payslip['employee_id'][0], 'name': payslip['employee_id'][1]}
        payslip['job_id'] = {'id': payslip['job_id'][0], 'name': payslip['job_id'][1]}
        payslip['level_id'] = {'id': payslip['level_id'][0], 'name': payslip['level_id'][1]}
        payslip['role_id'] = {'id': payslip['role_id'][0], 'name': payslip['role_id'][1]}

    return payslips


# Hàm lấy thông tin chi tiết của một bản ghi Payslip
def get_payslip_details(payslip_id):
    payslip = models.execute_kw(db, uid, password, 'hr.payslip', 'read', [payslip_id], {'fields': ['name', 'start_date', 'end_date', 'actual_working_hours', 'standard_working_hours', 'gross_salary', 'net_salary', 'state', 'employee_id', 'role_id', 'job_id', 'level_id']})
    payslip[0]['employee_id'] = {'id': payslip[0]['employee_id'][0], 'name': payslip[0]['employee_id'][1]}
    payslip[0]['role_id'] = {'id': payslip[0]['role_id'][0], 'name': payslip[0]['role_id'][1]}
    payslip[0]['job_id'] = {'id': payslip[0]['job_id'][0], 'name': payslip[0]['job_id'][1]}
    payslip[0]['level_id'] = {'id': payslip[0]['level_id'][0], 'name': payslip[0]['level_id'][1]}

    return payslip

# Dữ liệu mới cho việc tạo mới một bản ghi Payslip
payslip_data = {
    'name': 'New Payslip',
    'start_date': '2024-04-01',
    'end_date': '2024-04-30',
    'actual_working_hours': 160,
    'standard_working_hours': 176,
    'gross_salary': 5000.0,
    'net_salary': 4000.0,
    'state': 'new',
    'employee_id': 1,
    'role_id': 1,
    'job_id': 1,
    'level_id': 1
}

payslip_data_update = {
    'name': 'New Payslip',
    'start_date': '2024-04-01',
    'end_date': '2024-04-30',
    'actual_working_hours': 161,
    'standard_working_hours': 176,
    'gross_salary': 5000.0,
    'net_salary': 4000.0,
    'state': 'new',
    'employee_id': 1,
    'role_id': 1,
    'job_id': 1,
    'level_id': 1
}

# Sử dụng các hàm để thực hiện các thao tác CRUD
# payslip_id = create_payslip(payslip_data)
# update_payslip(payslip_id, payslip_data_update)
# delete_payslip(payslip_id)
print get_all_payslips()
# print get_payslip_details(35)

print "done"
