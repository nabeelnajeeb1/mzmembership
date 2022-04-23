frappe.pages['thank-you'].on_page_load = function(wrapper) {
	var page = frappe.ui.make_app_page({
		parent: wrapper,
		title: 'Thank You',
		single_column: true
	});
}