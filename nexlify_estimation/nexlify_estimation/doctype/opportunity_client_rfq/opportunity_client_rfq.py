# Copyright (c) 2026, Kamal Adel and contributors
# For license information, please see license.txt

# import frappe
from frappe.model.document import Document


class OpportunityClientRFQ(Document):
	# begin: auto-generated types
	# This code is auto-generated. Do not modify anything in this block.

	from typing import TYPE_CHECKING

	if TYPE_CHECKING:
		from frappe.types import DF

		nexlify_estimation_opportunity_rfq_description: DF.Data | None
		nexlify_estimation_opportunity_rfq_item: DF.Data | None
		nexlify_estimation_opportunity_rfq_quantity: DF.Float
		nexlify_estimation_opportunity_rfq_uom: DF.Link | None
		parent: DF.Data
		parentfield: DF.Data
		parenttype: DF.Data
	# end: auto-generated types

	pass
