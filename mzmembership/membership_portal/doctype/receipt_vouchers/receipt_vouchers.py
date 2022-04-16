# Copyright (c) 2022, m20zero and contributors
# For license information, please see license.txt
import frappe
from frappe.model.document import Document

class ReceiptVouchers(Document):
    def on_submit(self):
            self.make_gl()

    def on_cancel(self):
        self.cancel_gl()

    def make_gl(self):
        account = frappe.db.get_value("Party Type", self.party_type, "account")
        # if self.is_paid == 1 and self.mode_of_payment:
            # cash_account = frappe.db.get_value("Mode of Payment", self.mode_of_payment, "account")
        #     self.gl_entry(cash_account, self.total, "credit", self.party_type, self.party, self.name, "")
        #     self.gl_entry(account, self.total, "debit", self.party_type, self.party, self.name, "")
        # else:
        self.gl_entry(self.account, self.paid_amount, "credit", self.party_type, self.party, self.name,self.cost_center)
        for item in self.items:
            self.gl_entry(account, item.allocated, "debit", self.party_type, self.party, self.name,self.cost_center)

    def gl_entry(self,account, amount, en_type, party_type, party, name,cost_center):
        gl = frappe.get_doc(dict(doctype="GL Entry", posting_date=frappe.utils.nowdate(), transaction_date=frappe.utils.nowdate(), account=account, cost_center=cost_center,party_type=party_type, party=party, voucher_type="Receipt Vouchers", voucher_no=self.name,  remarks="No Remarks"))
        if(en_type == "credit"):
            gl.credit = amount
            gl.credit_in_account_currency = amount
        else:
            gl.debit = amount
            gl.debit_in_account_currency = amount
        gl.save(ignore_permissions=True)
        gl.submit()

    def cancel_gl(self):
        gl_entry = frappe.db.get_list("GL Entry", {"voucher_no": self.name, "voucher_type": "Receipt Vouchers", "docstatus": 1}, "name")
        for gl in gl_entry:
            doc = frappe.get_doc("GL Entry", gl.name)
            doc.cancel()
