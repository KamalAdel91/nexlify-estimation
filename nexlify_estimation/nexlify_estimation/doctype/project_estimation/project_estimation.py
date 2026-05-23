# Copyright (c) 2026, Kamal Adel and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document


class ProjectEstimation(Document):
    # begin: auto-generated types
    # This code is auto-generated. Do not modify anything in this block.

    from typing import TYPE_CHECKING

    if TYPE_CHECKING:
        from frappe.types import DF
        from nexlify_estimation.nexlify_estimation.doctype.project_estimation_tasks.project_estimation_tasks import ProjectEstimationTasks

        amended_from: DF.Link | None
        naming_series: DF.Literal["EST-.YYYY.-.#####."]
        nexlify_estimation_company_name: DF.Link | None
        nexlify_estimation_customer_name: DF.Link | None
        nexlify_estimation_date: DF.Date | None
        nexlify_estimation_opportunity: DF.Link | None
        nexlify_estimation_opportunity_date: DF.Date | None
        nexlify_estimation_tasks_table: DF.Table[ProjectEstimationTasks]
    # end: auto-generated types

    pass


@frappe.whitelist()
def get_opportunity_rfq_items(opportunity):
    doc = frappe.get_doc('Opportunity', opportunity)
    items = []
    for row in doc.get('custom_rfq_table', []):
        items.append({
            'opportunity_rfq_item': row.opportunity_rfq_item,
            'opportunity_rfq_description': row.opportunity_rfq_description,
            'opportunity_rfq_uom': row.opportunity_rfq_uom,
            'opportunity_rfq_quantity': row.opportunity_rfq_quantity,
        })
    return items