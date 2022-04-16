// Copyright (c) 2021, M20Zero and contributors
// For license information, please see license.txt

frappe.ui.form.on('Party Type', {
	// refresh: function(frm) {

	// }
	setup: function(frm){
		frm.set_query("account", function(doc){
			return {
				filters: [
					["Account", "is_group", "=", 0]
				]
			}
		});
	}
});
