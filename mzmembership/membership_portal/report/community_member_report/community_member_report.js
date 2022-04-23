// Copyright (c) 2016, Aadhil M20Zero and contributors
// For license information, please see license.txt
/* eslint-disable */

frappe.query_reports["Community Member Report"] = {
	"filters": [
		{
                        "fieldname": "name",
                        "label": __("ID"),
                        "fieldtype": "Link",
                        "options": "Community Member"
                },
                {
                        "fieldname": "full_name",
                        "label": __("Full Name"),
                        "fieldtype": "Data"
                },
		{
			"fieldname": "batch",
			"label": __("Batch"),
			"fieldtype": "Select",
			"options": "\n1984\n1985\n1986\n1987\n1988\n1989\n1990\n1991\n1992\n1993\n1994\n1995\n1996\n1997\n1998\n1999\n2000\n2001\n2002\n2003\n2004\n2005\n2006\n2007\n2008\n2009\n2010\n2011\n2012\n2013\n2014\n2015\n2016\n2017\n2018\n2019\n2020\n2021"
		},
		{
			"fieldname": "gender",
			"label": __("Gender"),
			"fieldtype": "Link",
			"options": "Gender"
		},
		{
			"fieldname": "mobile",
			"label": __("Mobile Number"),
			"fieldtype": "Data"
		},
		{
			"fieldname": "status",
			"label": __("Status"),
			"fieldtype": "Select",
			"options": "\nPending\nApproved\nRejected",
		}
	]
};
