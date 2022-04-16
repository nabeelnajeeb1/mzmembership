# Copyright (c) 2021, M20Zero and contributors
# For license information, please see license.txt

import frappe
from past.builtins import cmp
from frappe.utils.nestedset import NestedSet
from frappe.utils import cint, cstr, flt, formatdate, get_number_format_info, getdate, now, nowdate

class Account(NestedSet):
	pass

@frappe.whitelist()
def update_account_number(name, account_name, account_number=None, from_descendant=False):
	account = frappe.db.get_value("Account", name, "company", as_dict=True)
	if not account: return

	old_acc_name, old_acc_number = frappe.db.get_value('Account', name, \
				["account_name", "account_number"])

	# check if account exists in parent company
	ancestors = get_ancestors_of("Company", account.company)
	allow_independent_account_creation = frappe.get_value("Company", account.company, "allow_account_creation_against_child_company")

	if ancestors and not allow_independent_account_creation:
		for ancestor in ancestors:
			if frappe.db.get_value("Account", {'account_name': old_acc_name, 'company': ancestor}, 'name'):
				# same account in parent company exists
				allow_child_account_creation = _("Allow Account Creation Against Child Company")

				message = _("Account {0} exists in parent company {1}.").format(frappe.bold(old_acc_name), frappe.bold(ancestor))
				message += "<br>"
				message += _("Renaming it is only allowed via parent company {0}, to avoid mismatch.").format(frappe.bold(ancestor))
				message += "<br><br>"
				message += _("To overrule this, enable '{0}' in company {1}").format(allow_child_account_creation, frappe.bold(account.company))

				frappe.throw(message, title=_("Rename Not Allowed"))

	validate_account_number(name, account_number, account.company)
	if account_number:
		frappe.db.set_value("Account", name, "account_number", account_number.strip())
	else:
		frappe.db.set_value("Account", name, "account_number", "")
	frappe.db.set_value("Account", name, "account_name", account_name.strip())

	if not from_descendant:
		# Update and rename in child company accounts as well
		descendants = get_descendants_of('Company', account.company)
		if descendants:
			sync_update_account_number_in_child(descendants, old_acc_name, account_name, account_number, old_acc_number)

	new_name = get_account_autoname(account_number, account_name, account.company)
	if name != new_name:
		frappe.rename_doc("Account", name, new_name, force=1)
		return new_name

@frappe.whitelist()
def merge_account(old, new, is_group, root_type, company):
	# Validate properties before merging
	if not frappe.db.exists("Account", new):
		throw(_("Account {0} does not exist").format(new))

	val = list(frappe.db.get_value("Account", new,
		["is_group", "root_type", "company"]))

	if val != [cint(is_group), root_type, company]:
		throw(_("""Merging is only possible if following properties are same in both records. Is Group, Root Type, Company"""))

	if is_group and frappe.db.get_value("Account", new, "parent_account") == old:
		frappe.db.set_value("Account", new, "parent_account",
			frappe.db.get_value("Account", old, "parent_account"))

	frappe.rename_doc("Account", old, new, merge=1, force=1)

	return new

@frappe.whitelist()
def get_root_company(company):
	# return the topmost company in the hierarchy
	ancestors = get_ancestors_of('Company', company, "lft asc")
	return [ancestors[0]] if ancestors else []

def sync_update_account_number_in_child(descendants, old_acc_name, account_name, account_number=None, old_acc_number=None):
	filters = {
		"company": ["in", descendants],
		"account_name": old_acc_name,
	}
	if old_acc_number:
		filters["account_number"] = old_acc_number

	for d in frappe.db.get_values('Account', filters=filters, fieldname=["company", "name"], as_dict=True):
			update_account_number(d["name"], account_name, account_number, from_descendant=True)
