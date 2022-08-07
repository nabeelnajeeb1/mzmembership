# Copyright (c) 2022, m20zero and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document  


class Membership(Document):
    def on_submit(self):
        self.make_invoice()

    def make_invoice(self):
        self.invoice_entry(self.name, self.member, self.member_name, self.membership_type, self.amount, self.income_account)

    def invoice_entry(self, member,name,member_name,membership_type,amount,income_account):
        parent = frappe.get_doc(dict(doctype="Invoice",date=frappe.utils.nowdate(),party_type="member",party=name,party_name=member_name,total=amount,total_qty="1"))
        parent.append("items",{
            "item":membership_type,
            "qty":"1",
            "rate":amount,
            "income_account":income_account,
            "amount":amount,
        })
        parent.save(ignore_permissions=True)
       # parent.submit() 
