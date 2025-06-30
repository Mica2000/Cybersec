import frappe
from frappe import _


@frappe.whitelist(allow_guest=True)
def add_log():
    data = frappe.form_dict

    doc = frappe.get_doc({
        "doctype": "Security Log",
        "event_type": data.get("event_type"),
        "source_ip": data.get("source_ip"),
        "message": data.get("message"),
        "severity": data.get("severity"),
        "timestamp": frappe.utils.now_datetime(),
        "status": "New"
    })
    doc.insert(ignore_permissions=True)
    return {
        "status": "success",
        "name": doc.name,
        "source_ip": doc.source_ip,
        "message": doc.message,
        "severity": doc.severity,
        "timestamp": doc.timestamp
    }
