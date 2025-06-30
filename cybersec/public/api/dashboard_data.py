import frappe
from frappe.utils import now_datetime
from collections import defaultdict
from datetime import datetime


@frappe.whitelist()
def get_dashboard_data():
    logs = frappe.get_all("Security Log",
                          fields=["severity", "event_type", "timestamp"])

    severity_counts = defaultdict(int)
    event_type_counts = defaultdict(int)
    timeline_map = defaultdict(int)

    for log in logs:
        severity_counts[log.severity] += 1
        event_type_counts[log.event_type] += 1

        date_key = log.timestamp.date().isoformat()
        timeline_map[date_key] += 1

    timeline = {
        "labels": list(timeline_map.keys()),
        "values": list(timeline_map.values())
    }

    return {
        "severity_counts": dict(severity_counts),
        "event_type_counts": dict(event_type_counts),
        "timeline": timeline
    }
