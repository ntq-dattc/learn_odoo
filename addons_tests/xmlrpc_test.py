# -*- coding: utf-8 -*-
try:
    from xmlrpc import client as xmlrpclib
except:
    import xmlrpclib
from flask import Flask, render_template

app = Flask(__name__)

url = 'http://d-sdc1-dungnm1.ntq-solution.com.vn:8069'
db = 'pythonOdoo'
username = 'admin'
password = '1'

common = xmlrpclib.ServerProxy('{}/xmlrpc/2/common'.format(url))
uid = common.authenticate(db, username, password, {})

models = xmlrpclib.ServerProxy('{}/xmlrpc/2/object'.format(url))

def create_contract(data):
    contract_id = models.execute_kw(db, uid, password, 'hop.dong', 'create', [data])
    return contract_id

def update_contract(contract_id, data):
    models.execute_kw(db, uid, password, 'hop.dong', 'write', [[contract_id], data])
    return True

def get_all_contracts():
    contracts = models.execute_kw(
        db, uid, password, 'hop.dong', 'search_read', [[]], {'fields': ['name', 'start_date', 'end_date', 'contract_type', 'signed_date', 'salary_rack', 'efficiency_wage', 'status', 'employee_id']}
    )

    contract_data = {}
    for contract in contracts:
        contract_id = contract['id']
        contract_data[contract_id] = {
            'name': contract['name'],
            'start_date': contract['start_date'],
            'end_date': contract['end_date'],
            'contract_type': contract['contract_type'],
            'signed_date': contract['signed_date'],
            'salary_rack': contract['salary_rack'],
            'efficiency_wage': contract['efficiency_wage'],
            'status': contract['status'],
            'employee_id': contract['employee_id'],
        }
    return contract_data


def delete_contract(contract_id):
    models.execute_kw(db, uid, password, 'hop.dong', 'unlink', [[contract_id]])
    return True


def get_contract_details(payslip_id):
    contract = models.execute_kw(
        db, uid, password, 'hop.dong', 'read', [payslip_id], {
            'fields': ['name', 'start_date', 'end_date', 'contract_type', 'signed_date', 'salary_rack',
                       'efficiency_wage', 'status', 'employee_id']}
    )

    contract_data = {
        'name': contract['name'],
        'start_date': contract['start_date'],
        'end_date': contract['end_date'],
        'contract_type': contract['contract_type'],
        'signed_date': contract['signed_date'],
        'salary_rack': contract['salary_rack'],
        'efficiency_wage': contract['efficiency_wage'],
        'status': contract['status'],
        'employee_id': contract['employee_id'],
    }

    return contract_data


@app.route('/contract')
def index():
    contracts = get_all_contracts()

    return render_template('index.html', contracts=contracts)

if _name_ == '__main__':
    app.run(debug=True)