# Copyright (c) 2013, M20Zero and contributors
# For license information, please see license.txt

import frappe
from frappe import _, msgprint

def execute(filters=None):
    columns, data = [], []
    columns = get_columns()
    data = get_data(filters)
    return columns, data


def get_columns():
    columns = [
            {
                "label": _("Posting Date"),
                "fieldname": "posting_date",
                "fieldtype": "Date",
                "width": 100
            },
            {
                "label": _("Account"),
                "fieldname": "account",
                "fieldtype": "Link",
                "options": "Account",
                "width": 150
            },
            {
                "label": _("Debit"),
                "fieldname": "debit",
                "fieldtype": "Currency",
                "width": 150
            },
            {
                "label": _("Credit"),
                "fieldname": "credit",
                "fieldtype": "Currency",
                "width": 150
            },
            {
                "label": _("Voucher Type"),
                "fieldname": "voucher_type",
                "fieldtype": "Data",
                "width": 150
            },
            {
                "label": _("Voucher No"),
                "fieldname": "voucher_no",
                "fieldtype": "Data",
                "width": 150
            },
            {
                "label": _("Party Type"),
                "fieldname": "party_type",
                "fieldtype": "Data",
                "width": 150
            },
            {
                "label": _("Party"),
                "fieldname": "party",
                "width": 150
            },
            {
                "label": _("Project"),
                "fieldname": "project",
                "fieldtype": "Data",
                "width": 150
            },
            {
                "label": _("Remarks"),
                "fieldname": "remarks",
                "fieldtype": "Data",
                "width": 150
            }
    ]
    return columns


def get_conditions(filters):
    try:
        condition = ""
        if(filters.get("from_date") and filters.get("to_date")):
            condition += " and posting_date between '%s' and '%s'"%(filters.get("from_date"), filters.get("to_date"))

        if(filters.get("voucher_no")):
            condition += " and voucher_no = %s "%(filters.get("voucher_no"))

        if(filters.get("account")):
            condition += " and account = %s "%(filters.get("account"))
        return condition
    except Exception as e:
        frappe.msgprint(e)

def get_data(filters):
    try:
        condition = get_conditions(filters)
        data = frappe.db.sql("""select posting_date, account, debit, credit, party_type, party, voucher_type, voucher_no, project, remarks from `tabGL Entry` where docstatus = 1 %s """%condition, filters, as_dict=True)
        return data
    except Exception as e:
        frappe.msgprint(e)
