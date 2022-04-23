# Copyright (c) 2013, Aadhil M20Zero and contributors
# For license information, please see license.txt

import frappe
from frappe import _

def execute(filters=None):
    columns, data = [], []

    columns = get_columns(filters)
    rows = get_data(filters)

    for r in rows:
        data.append([r['name'], r['full_name'], r['date_of_birth'], r['gender'], r['batch_pass_out'], r['stream'], r['mobile_number'], r['email'], r['residence'], r['status']])
    return columns, data


def get_columns(filters):
    columns = [_("ID") + ":Data:150"] + [_("Full Name") + ":Data:150"] + [_("Date of Birth") + ":Date:150"]  + [_("Gender") + ":Data:110"] + [_("Batch") + ":Data:100"] + [_("Stream") + ":Data:100"] + [_("Mobile") + ":Data:100"] + [_("Email") + ":Data:100"] + [_("Residency") + ":Data:100"] + [_("Status") + ":Data:100"]

    return columns


def get_condition(filters):
    condition = ""

    if(filters.get("batch")):
        condition += " and batch_pass_out = %(batch)s"

    if(filters.get("gender")):
        condition += " and gender = %(gender)s"

    if(filters.get("mobile")):
        condition += " and mobile_number = %(mobile)s"

    if(filters.get("status")):
        condition += " and status = %(status)s"

    if(filters.get("name")):
        condition += " and name = %(name)s"

    if(filters.get("full_name")):
        condition += " and full_name = %(full_name)s"

    return condition

def get_data(filters):
    condition = get_condition(filters)

    data = frappe.db.sql("""select name, full_name, date_of_birth, gender, batch_pass_out, stream, mobile_number, email, residence, status from `tabCommunity Member` where docstatus != 2 %s """%condition, filters, as_dict=True)

    return data
