// Copyright (c) 2022, m20zero and contributors
// For license information, please see license.txt

frappe.ui.form.on("Member", "validate", function(frm, cdt, cdn) { 
	var dt17 = frappe.get_doc(cdt,cdn);
			 if (frm.doc.date_of_birth){
				if (frm.doc.date_of_birth > frappe.datetime.get_today()){
				   frappe.msgprint(__("Enter a valid Date of Birth"));
				   frappe.validated = false;
				}
			}
});
frappe.ui.form.on("Member", "validate", function(frm, cdt, cdn) { 
	var dt16 = frappe.get_doc(cdt,cdn);
			 if (frm.doc.membership_expiry_date){
				if (frm.doc.membership_expiry_date < frm.doc.member_since ){
				   frappe.msgprint(__("Membership Expiry  must be greater tham member since"));
				   membership_expiry_date
				}
			}
})
frappe.ui.form.on('Member',{
	refresh: function(frm) {				
		if (frm.doc.membership_expiry_date){
			if (frm.doc.membership_expiry_date == frappe.datetime.get_today() ){
				frm.add_custom_button(__("Renew"), function(){
				
					let doc = frappe.model.get_new_doc("Membership");
					doc.member = cur_frm.doc.name;
					doc.series = "MS-.YY.-";
					doc.member_name = cur_frm.doc.full_name;
					doc.membership_type = cur_frm.doc.membership_type;
					doc.status = "Renewed";
					doc.valid_from = cur_frm.doc.member_since;
					doc.valid_to = cur_frm.doc.membership_expiry_date;
					doc.amount = cur_frm.doc.amount ;
					frappe.set_route("FORM", doc.doctype, doc.name);
				
				});
			
	
			}
		}
	}
});
frappe.ui.form.on("Member", {
	refresh: function(frm) {
	
			frm.add_custom_button(__("Create Membership"), function(){
				if(cur_frm.is_dirty()){
					frappe.msgprint("Please save the form before creating Membership")
				}else{
					let doc = frappe.model.get_new_doc("Membership");
					doc.member = cur_frm.doc.name;
					doc.series = "MS-.YY.-";
					doc.member_name = cur_frm.doc.full_name;
					doc.membership_type = cur_frm.doc.membership_type;
					doc.status = "New";
					doc.valid_from = cur_frm.doc.member_since;
					doc.valid_to = cur_frm.doc.membership_expiry_date;
					doc.amount = cur_frm.doc.amount ;
					frappe.set_route("FORM", doc.doctype, doc.name);
					
				}
			});
		
	}
});

