// Copyright (c) 2022, m20zero and contributors
// For license information, please see license.txt

frappe.ui.form.on("Expense Entry Item", "rate",function(frm,cdt,cdn)
{
	var d = locals[cdt][cdn];
	d.amount = d.qty*d.rate;
	var table = frm.doc.items;
	var total = 0;

	for(var i in table) {
		total = total + Number(table[i].amount);
	}
 	frm.set_value("total",total);
	 frm.set_value("net_total",total);
	 frm.set_value("grand_total",total);

	cur_frm.refresh();
 });
frappe.ui.form.on("Expense Entry Item", "qty", function(frm, cdt, cdn) {

	var table = frm.doc.items;
	var total = 0;
	for(var i in table) {
		total = total + Number(table[i].qty);
	}
 
	 frm.set_value("total_quantity",total);
	frm.set_value("net_total",total);
	frm.set_value("grand_total",total);
	cur_frm.refresh();
});


frappe.ui.form.on("Expense Entry",{
	grand_total: function(frm){
		var a = frm.doc.net_total - frm.doc.additional_discount_amount;
		frm.set_value("grand_total", a);
		frm.refresh_field("grand_total");
	}
});





frappe.ui.form.on("Expense Entry",{
	expense_head: function(frm){
	if(frm.doc.expense_head){
			if(frm.doc.items && !cur_frm.doc.items[0].expense_head){
					frappe.model.set_value(cur_frm.doc.items[0].doctype, cur_frm.doc.items[0].name, "expense_head", frm.doc.expense_head);
			}
	}
}
});
frappe.ui.form.on("Expense Entry", {
	refresh: function(frm) {
		if(cur_frm.doc.docstatus == 1){
			frm.add_custom_button(__("Make Payment Voucher"), function(){
				if(cur_frm.is_dirty()){
					frappe.msgprint("Please save the form before creating Payment Voucher")
				}else{
					let doc = frappe.model.get_new_doc("Payment Voucher");
					doc.posting_date = frappe.datetime.now_date();
					doc.naming_series = "RV-.YY.-";
					doc.party_type = cur_frm.doc.party_type;
					doc.party = cur_frm.doc.party;
					doc.party_name = cur_frm.doc.party_name;
					let child = frappe.model.get_new_doc("Payment Item", doc, "items");
					$.extend(child, {
						"expense": cur_frm.doc.name,
						"date": cur_frm.doc.date,
						"total":cur_frm.doc.total
					});
					doc.total_qty = 1;
					doc.total = cur_frm.doc.amount;
					frappe.set_route("FORM", doc.doctype, doc.name);
				}
			});
		}
	},
	setup: function(frm){
                frm.set_query("party_type", function(doc) {
                        return {
                                filters: [
                                        ["DocType", "name", "in", ["Member"]]
                                ]
                        }
                });

                /*frm.set_query("account", function(doc) {
                        return {
                                filters: [
                                        ["Account", "is_group", "=", 0]
                                ]
                        }
                });*/
        }
});
