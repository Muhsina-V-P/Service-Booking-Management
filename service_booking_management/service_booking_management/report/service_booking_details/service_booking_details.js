// Copyright (c) 2025, Muhsina and contributors
// For license information, please see license.txt

frappe.query_reports["Service Booking Details"] = {
    "filters": [
        {
            "fieldname": "service_type",
            "label": "Service Type",
            "fieldtype": "Select",
			"options": "\nTherapy\nSpa\nOthers",
            "reqd": 0
        },
        {
            "fieldname": "status",
            "label": "Status",
            "fieldtype": "Select",
            "options": "\nRequested\nApproved\nCompleted",
            "reqd": 0
        }
    ]
};
