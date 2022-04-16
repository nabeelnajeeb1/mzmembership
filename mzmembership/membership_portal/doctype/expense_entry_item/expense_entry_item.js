// Copyright (c) 2022, M20Zero and contributors
// For license information, please see license.txt

frappe.ui.form.on('Expense Entry Item', {
	refresh: function(frm) {
		timezone = frm.get_value('Expense Entry', 'expense_head')
		frm.set_value("expense_head",timezone);

	}
});
