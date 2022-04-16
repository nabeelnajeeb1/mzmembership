import frappe 
from frappe import _
import functools
import math
import re
from past.builtins import cmp
from frappe.utils import cint, cstr, flt, formatdate, get_number_format_info, getdate, now, nowdate

def sort_accounts(accounts, is_root=False, key="name"):
    """Sort root types as Asset, Liability, Equity, Income, Expense"""
    
    def compare_accounts(a, b):
        if re.split(r'\W+', a[key])[0].isdigit():
            # if chart of accounts is numbered, then sort by number
            return cmp(a[key], b[key])
        elif is_root:
            if a.report_type != b.report_type and a.report_type == "Balance Sheet":
                return -1
            if a.root_type != b.root_type and a.root_type == "Asset":
                return -1
            if a.root_type == "Liability" and b.root_type == "Equity":
                return -1
            if a.root_type == "Income" and b.root_type == "Expense":
                return -1
        else:
            # sort by key (number) or name
            return cmp(a[key], b[key])
        return 1
    
    accounts.sort(key = functools.cmp_to_key(compare_accounts))


@frappe.whitelist()
def get_children(doctype, parent, organization, is_root=False):
    parent_fieldname = 'parent_' + doctype.lower().replace(' ', '_')
    fields = [
            'name as value',
            'is_group as expandable'
    ]
    filters = [['docstatus', '<', 2]]
    
    filters.append(['ifnull(`{0}`,"")'.format(parent_fieldname), '=', '' if is_root else parent])
    if is_root:
        fields += ['root_type', 'report_type', 'account_currency'] if doctype == 'Account' else []
        filters.append(['organization', '=', organization])
    else:
        fields += ['root_type', 'account_currency'] if doctype == 'Account' else []
        fields += [parent_fieldname + ' as parent']
        
    acc = frappe.get_list(doctype, fields=fields, filters=filters)
    
    if doctype == 'Account':
        sort_accounts(acc, is_root, key="value")
        
    return acc

@frappe.whitelist()
def add_ac(args=None):
    from frappe.desk.treeview import make_tree_args
    if not args:
        args = frappe.local.form_dict
        
    args.doctype = "Account"
    args = make_tree_args(**args)
    ac = frappe.new_doc("Account")
    
    if args.get("ignore_permissions"):
        ac.flags.ignore_permissions = True
        args.pop("ignore_permissions")
    
    ac.update(args)
    if not ac.parent_account:
        ac.parent_account = args.get("parent")
        
    ac.old_parent = ""
    ac.freeze_account = "No"
    if cint(ac.get("is_root")):
        ac.parent_account = None
        ac.flags.ignore_mandatory = True
        
    ac.insert()


@frappe.whitelist()
def get_account_balances(accounts, organization):
    if isinstance(accounts, string_types):
        accounts = loads(accounts)
        
    if not accounts:
        return []
    
    company_currency = frappe.get_cached_value("Organization",  organization,  "default_currency")
    for account in accounts:
        account["company_currency"] = company_currency
        account["balance"] = flt(get_balance_on(account["value"], in_account_currency=False, company=company))
        if account["account_currency"] and account["account_currency"] != company_currency:
            account["balance_in_account_currency"] = flt(get_balance_on(account["value"], company=company))
            
    return accounts
