// Copyright (c) 2016, M20Zero and contributors
// For license information, please see license.txt
/* eslint-disable */

frappe.query_reports["Ledger"] = {
	"filters": [
		{
			"fieldname": "from_date",
			"label": __("rom Date"),
			"fieldtype": "Date",
			"default": "Today",
			"reqd": 1
		},
		{
			"fieldname": "to_date",
			"label": __("To Date"),
			"fieldtype": "Date",
			"default": "Today",
			"reqd": 1
		},
		{
			"fieldname": "voucher_no",
			"label": __("Voucher No"),
			"fieldtype": "Data",
			"reqd": 0
		},
		{
			"fieldname": "account",
			"label": __("Account"),
			"fieldtype": "Link",
			"options": "Account",
			"reqd": 0
		},
	]
};
