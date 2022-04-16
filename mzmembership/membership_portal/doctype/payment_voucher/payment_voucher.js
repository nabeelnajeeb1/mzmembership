// Copyright (c) 2022, m20zero and contributors
// For license information, please see license.txt

frappe.ui.form.on("Payment Item", "outstanding",function(frm,cdt,cdn)
{
	var d = locals[cdt][cdn];
	d.outstanding =d.total-d.allocated;
	total=d.outstanding;
	frm.set_value("d.allocated",total);
	frm.refresh_field("items")
	cur_frm.refresh();
});
frappe.ui.form.on("Payment Voucher",{
	paid_amount: function(frm){
	if(frm.doc.paid_amount){
			if(frm.doc.items && !cur_frm.doc.items[0].allocated){
					frappe.model.set_value(cur_frm.doc.items[0].doctype, cur_frm.doc.items[0].name, "allocated", frm.doc.paid_amount);
			}
	}
}
});