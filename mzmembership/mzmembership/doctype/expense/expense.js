// Copyright (c) 2022, M20Zero and contributors
// For license information, please see license.txt


frappe.ui.form.on("Expense Item", "amount", function(frm, cdt, cdn) {

   var table = frm.doc.expense_table;
   var total = 0;
   for(var i in table) {
       total = total + Number(table[i].amount);
   }

	frm.set_value("total",total);
        
});


frappe.ui.form.on('Expense', {
	// refresh: function(frm) {

	// }
	setup: function(frm){
		frm.set_query("party_type", function(){
			return{
				query: "mzmembership.whitelisted.get_party"
			}
		});
	}
});

