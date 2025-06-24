# Copyright (c) 2025, Muhsina and contributors
# For license information, please see license.txt
import frappe
from frappe.utils import formatdate

def execute(filters=None):
    columns = get_columns()
    data = get_data(filters)
    return columns, data

def get_columns():
    return [
        {"label": "Booking ID", "fieldname": "name", "fieldtype": "Link", "options": "Service Booking", "width": 120},
        {"label": "Customer Name", "fieldname": "customer_name", "fieldtype": "Data", "width": 150},
        {"label": "Service Type", "fieldname": "service_type", "fieldtype": "Data", "width": 120},
        {"label": "Status", "fieldname": "status", "fieldtype": "Data", "width": 100},
        {"label": "Preferred Date & Time", "fieldname": "preferred_date_and_time", "fieldtype": "Datetime", "width": 180},
    ]

def get_data(filters):
    conditions = ""
    if filters.get("service_type"):
        conditions += " AND service_type = %(service_type)s"
    if filters.get("status"):
        conditions += " AND status = %(status)s"

    return frappe.db.sql(f"""
        SELECT
            name,
            customer_name,
            service_type,
            status,
            preferred_date_and_time
        FROM
            `tabService Booking`
        WHERE
            1 = 1 {conditions}
        ORDER BY
            creation DESC
    """, filters, as_dict=True)

