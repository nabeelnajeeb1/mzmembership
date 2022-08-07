import frappe
from frappe import _

#boot update
def update_boot(boot):
    try:
        data = frappe._dict({
            "company": get_user_info()
        })
        boot.update({"mes":data})
    except Exception as e:
        print(e)
        frappe.log_error(frappe.get_traceback(), "boot error")

def get_user_info():
    try:
        company = []
        com = frappe.db.get_list("Organization", ["name"])
        for c in com:
            company.append(c.name)
        return company
    except Exception as e:
        return []
