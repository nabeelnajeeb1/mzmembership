// Copyright (c) 2022, m20zero and contributors
// For license information, please see license.txt

frappe.ui.form.on("Sponsor", {
	refresh: function(frm) {
		if(cur_frm.doc.docstatus == 1){
			frm.add_custom_button(__("Make Invoice"), function(){
				if(cur_frm.is_dirty()){
					frappe.msgprint("Please save the form before creating Invoice")
				}else{
					let doc = frappe.model.get_new_doc("Invoice");
					doc.date = frappe.datetime.now_date();
					doc.naming_series = "INV-.YY.-";
					doc.party_type = "Sponsor";
					doc.party = cur_frm.doc.name;
					doc.party_name = cur_frm.doc.sponsor_name;
					let child = frappe.model.get_new_doc("Invoice Item", doc, "items");
					$.extend(child, {
						"item": "",
						"qty": 1,
						"rate": 0,
						"amount": 0,
						"income_account": cur_frm.doc.income_account
					});
					doc.total_qty = 1;
					doc.total = cur_frm.doc.amount;
					frappe.set_route("FORM", doc.doctype, doc.name);
				}
			});
		}
	}
});
