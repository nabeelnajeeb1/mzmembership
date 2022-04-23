from __future__ import unicode_literals

import frappe
from frappe import _

def get_context(context):
	# do your magic here
	pass


@frappe.whitelist(allow_guest=True)
def check_user(email):
    try:
        if(frappe.db.exists("Community Member", {"email": email})):
            return True
        else:
            return False
    except Exception as e:
        frappe.msgprint(e)
