import frappe

@frappe.whitelist(allow_guest=True)
@frappe.validate_and_sanitize_search_inputs
def get_party(doctype, txt, searchfield, start, page_len, filters):
    return frappe.db.sql(""" select name from `tabDocType` where name in(select name from `tabParty Type`) """)
