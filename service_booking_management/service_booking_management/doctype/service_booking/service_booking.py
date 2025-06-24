# Copyright (c) 2025, Muhsina and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document

class ServiceBooking(Document):
    def before_save(self):
        #print("1111111111111111111111")
        if self.status == "Approved" and not self.email_sent:
            #print("22222222222222222222222222")
            frappe.sendmail(
                recipients=[self.customer_email],
                subject="Service Booking Approved",
                message=f"""
                    <p>Dear {self.customer_name},</p>
                    <p>Your service booking has been <strong>approved</strong>.</p>
                    <p>Thank you for choosing us!</p>
                """
            )
            self.email_sent = 1
