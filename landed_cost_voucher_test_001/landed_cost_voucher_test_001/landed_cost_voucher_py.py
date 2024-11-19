# Copyright (c) 2024, Mahmoud Khattab
# For license information, please see license.txt

import frappe
from frappe.model.document import Document
from frappe import _

import json
from frappe.utils import flt

from frappe.exceptions import ValidationError


@frappe.whitelist()
def create_print_msg(doc, method=None):
    frappe.msgprint(str("Landed Cost Voucher Test 001 has been created."), alert=True)
    # doc.reload()



# journal_entry.submit()









# ==============================================================



@frappe.whitelist()
def create_journal_entry_from_lcv(lcv_name):
    lcv_doc = frappe.get_doc("Landed Cost Voucher", lcv_name)

    if not lcv_doc.opposite_account_link_a_001:
        frappe.throw("Opposite Account is required.")

    total_amount = lcv_doc.total_taxes_and_charges

    journal_entry = frappe.get_doc({
        "doctype": "Journal Entry",
        "voucher_type": "Cash Entry",
        "posting_date": lcv_doc.posting_date,
        "company": lcv_doc.company,
        "accounts": [
            {
                "account": "1111 - صندوق الفروع - KH",
                "debit_in_account_currency": total_amount,
                "credit_in_account_currency": 0,
            },
            {
                "account": lcv_doc.opposite_account_link_a_001,
                "debit_in_account_currency": 0,
                "credit_in_account_currency": total_amount,
            },
        ],
    })

    journal_entry.insert()

    # journal_entry.submit()

    return journal_entry.name












# @frappe.whitelist()
# def create_journal_entry_from_lcv_on_validate(doc, method):
#     if doc.get("journal_entry_reference"):
#         return doc.journal_entry_reference
#
#     if not doc.opposite_account_link_a_001:
#         frappe.throw("Opposite Account is required.")
#
#     total_amount = doc.total_taxes_and_charges
#
#     journal_entry = frappe.get_doc({
#         "doctype": "Journal Entry",
#         "voucher_type": "Cash Entry",
#         "posting_date": doc.posting_date,
#         "company": doc.company,
#         "accounts": [
#             {
#                 "account": "1111 - صندوق الفروع - KH",
#                 "debit_in_account_currency": total_amount,
#                 "credit_in_account_currency": 0,
#             },
#             {
#                 "account": doc.opposite_account_link_a_001,
#                 "debit_in_account_currency": 0,
#                 "credit_in_account_currency": total_amount,
#             },
#         ],
#     })
#
#     journal_entry.insert()
#     # journal_entry.submit()
#
#     # doc.db_set("journal_entry_reference", journal_entry.name)
#
#     return journal_entry.name























# Check create it temporarily
# Temporarily set it to None





# @frappe.whitelist()
# def create_journal_entry_from_lcv_on_validate(doc, method):
#     if not doc.get("journal_entry_reference"):
#         doc.set("journal_entry_reference", None)
#
#     if doc.journal_entry_reference:
#         return doc.journal_entry_reference
#
#     if not doc.opposite_account_link_a_001:
#         frappe.throw("Opposite Account is required.")
#
#
#
#     landed_cost_purchase_receipt = frappe.get_all(
#         "Landed Cost Purchase Receipt",
#         filters={"parent": doc, },
#         fields=["receipt_document_type", "receipt_document", "supplier", "posting_date", "grand_total"],
#     )
#
#     doc_receipt_document_type = landed_cost_purchase_receipt[0].get('receipt_document_type')
#     doc_receipt_document = landed_cost_purchase_receipt[0].get('receipt_document')
#     doc_supplier = landed_cost_purchase_receipt[0].get('supplier')
#     doc_posting_date = landed_cost_purchase_receipt[0].get('posting_date')
#     doc_grand_total = landed_cost_purchase_receipt[0].get('grand_total')
#
#
#     # frappe.msgprint(str(doc_receipt_document_type))
#     # frappe.msgprint(str(doc_receipt_document))
#     # frappe.msgprint(str(doc_supplier))
#     # frappe.msgprint(str(doc_posting_date))
#     # frappe.msgprint(str(doc_grand_total))
#
#
#
#     total_amount = doc.total_taxes_and_charges
#
#     journal_entry = frappe.get_doc({
#         "doctype": "Journal Entry",
#         "voucher_type": "Cash Entry",
#         "posting_date": doc.posting_date,
#         "company": doc.company,
#         "accounts": [
#             {
#                 "account": "1111 - صندوق الفروع - KH",
#                 "debit_in_account_currency": total_amount,
#                 "credit_in_account_currency": 0,
#             },
#             {
#                 "account": doc.opposite_account_link_a_001,
#                 "debit_in_account_currency": 0,
#                 "credit_in_account_currency": total_amount,
#             },
#         ],
#     })
#
#     journal_entry.insert()
#
#     # journal_entry.submit()
#
#     return journal_entry.name




#  ---------------------------------------------------------








#
# @frappe.whitelist()
# def create_journal_entry_from_lcv_on_validate(doc, method):
#     if not doc.get("journal_entry_reference"):
#         doc.set("journal_entry_reference", None)
#
#     if doc.journal_entry_reference:
#         return doc.journal_entry_reference
#
#     if not doc.opposite_account_link_a_001:
#         frappe.throw("Opposite Account is required.")
#
#     landed_cost_purchase_receipt = frappe.get_all(
#         "Landed Cost Purchase Receipt",
#         filters={"parent": doc},
#         fields=["receipt_document_type", "receipt_document", "supplier", "posting_date", "grand_total"],
#     )
#
#     doc_receipt_document_type = landed_cost_purchase_receipt[0].get('receipt_document_type')
#     doc_receipt_document = landed_cost_purchase_receipt[0].get('receipt_document')
#     doc_supplier = landed_cost_purchase_receipt[0].get('supplier')
#     doc_posting_date = landed_cost_purchase_receipt[0].get('posting_date')
#     doc_grand_total = landed_cost_purchase_receipt[0].get('grand_total')
#
#     total_amount = doc.total_taxes_and_charges
#
#     accounts = [
#         {
#             "account": "1111 - صندوق الفروع - KH",
#             "debit_in_account_currency": total_amount,
#             "credit_in_account_currency": 0,
#         }
#     ]
#
#     if doc.opposite_account_link_a_001 == "2110 - الدائنين - KH":
#         accounts.append({
#             "party_type": "Supplier",
#             "party": doc_supplier,
#             "account": doc.opposite_account_link_a_001,
#             "debit_in_account_currency": 0,
#             "credit_in_account_currency": total_amount,
#         })
#     else:
#         accounts.append({
#             "account": doc.opposite_account_link_a_001,
#             "debit_in_account_currency": 0,
#             "credit_in_account_currency": total_amount,
#         })
#
#     journal_entry = frappe.get_doc({
#         "doctype": "Journal Entry",
#         "voucher_type": "Cash Entry",
#         "posting_date": doc.posting_date,
#         "company": doc.company,
#         "accounts": accounts,
#     })
#
#     journal_entry.insert()
#
#     return journal_entry.name
#
#


# ====================  1  ====================





# @frappe.whitelist()
# def create_journal_entry_from_lcv_on_validate(doc, method):
#     if not doc.opposite_account_link_a_001:
#         frappe.throw("Opposite Account is required.")
#
#     landed_cost_purchase_receipt = frappe.get_all(
#         "Landed Cost Purchase Receipt",
#         filters={"parent": doc},
#         fields=["receipt_document_type", "receipt_document", "supplier", "posting_date", "grand_total"],
#     )
#
#     doc_receipt_document_type = landed_cost_purchase_receipt[0].get('receipt_document_type')
#     doc_receipt_document = landed_cost_purchase_receipt[0].get('receipt_document')
#     doc_supplier = landed_cost_purchase_receipt[0].get('supplier')
#     doc_posting_date = landed_cost_purchase_receipt[0].get('posting_date')
#     doc_grand_total = landed_cost_purchase_receipt[0].get('grand_total')
#
#     total_amount = doc.total_taxes_and_charges
#
#     accounts = [
#         {
#             "account": "1111 - صندوق الفروع - KH",
#             "debit_in_account_currency": total_amount,
#             "credit_in_account_currency": 0,
#         }
#     ]
#
#     if "2110 - الدائنين" in doc.opposite_account_link_a_001:
#         accounts.append({
#             "party_type": "Supplier",
#             "party": doc_supplier,
#             "account": doc.opposite_account_link_a_001,
#             "debit_in_account_currency": 0,
#             "credit_in_account_currency": total_amount,
#         })
#     else:
#         accounts.append({
#             "account": doc.opposite_account_link_a_001,
#             "debit_in_account_currency": 0,
#             "credit_in_account_currency": total_amount,
#         })
#
#
#     journal_entry = frappe.get_doc({
#         "doctype": "Journal Entry",
#         "voucher_type": "Cash Entry",
#         "posting_date": doc.posting_date,
#         "company": doc.company,
#         "accounts": accounts,
#     })
#
#     journal_entry.insert()
#     frappe.db.commit()
#
#     return journal_entry.name





# ====================  2  ====================





# @frappe.whitelist()
# def create_journal_entry_from_lcv_on_validate(doc, method):
#     if not doc.opposite_account_link_a_001:
#         frappe.throw("Opposite Account is required.")
#
#     landed_cost_purchase_receipt = frappe.get_all(
#         "Landed Cost Purchase Receipt",
#         filters={"parent": doc},
#         fields=["receipt_document_type", "receipt_document", "supplier", "posting_date", "grand_total"],
#     )
#
#     doc_receipt_document_type = landed_cost_purchase_receipt[0].get('receipt_document_type')
#     doc_receipt_document = landed_cost_purchase_receipt[0].get('receipt_document')
#     doc_supplier = landed_cost_purchase_receipt[0].get('supplier')
#     doc_posting_date = landed_cost_purchase_receipt[0].get('posting_date')
#     doc_grand_total = landed_cost_purchase_receipt[0].get('grand_total')
#
#     total_amount = doc.total_taxes_and_charges
#
#     accounts = [
#         # {
#         #     "account": "1111 - صندوق الفروع - KH",
#         #     "debit_in_account_currency": total_amount,
#         #     "credit_in_account_currency": 0,
#         # }
#     ]
#
#     if "2110 - الدائنين" in doc.opposite_account_link_a_001:
#         accounts.append({
#             "party_type": "Supplier",
#             "party": doc_supplier,
#             "account": doc.opposite_account_link_a_001,
#             "debit_in_account_currency": 0,
#             "credit_in_account_currency": total_amount,
#         })
#     else:
#         accounts.append({
#             "account": doc.opposite_account_link_a_001,
#             "debit_in_account_currency": 0,
#             "credit_in_account_currency": total_amount,
#         })
#
#
#     journal_entry = frappe.get_doc({
#         "doctype": "Journal Entry",
#         "voucher_type": "Cash Entry",
#         "posting_date": doc.posting_date,
#         "company": doc.company,
#         "accounts": accounts,
#     })
#
#     journal_entry.insert()
#     frappe.db.commit()
#
#     return journal_entry.name









#
# @frappe.whitelist()
# def create_journal_entry_from_lcv_on_validate(doc, method):
#     if not doc.opposite_account_link_a_001:
#         frappe.throw("Opposite Account is required.")
#
#     landed_cost_purchase_receipt = frappe.get_all(
#         "Landed Cost Purchase Receipt",
#         filters={"parent": doc.name},
#         fields=["receipt_document_type", "receipt_document", "supplier", "posting_date", "grand_total"],
#     )
#
#     if not landed_cost_purchase_receipt:
#         frappe.throw("Landed Cost Purchase Receipt not found.")
#
#     doc_supplier = landed_cost_purchase_receipt[0].get('supplier')
#     total_amount = doc.total_taxes_and_charges
#
#     accounts = []
#
#
#     accounts.append({
#         "account": frappe.db.get_value("Account", {"account_type": "Temporary"}, "name") or frappe.throw(
#             "Please create a 'Temporary' account type in COA for virtual debit handling."
#         ),
#         "debit_in_account_currency": total_amount,
#         "credit_in_account_currency": 0,
#     })
#
#     if "2110 - الدائنين" in doc.opposite_account_link_a_001:
#         accounts.append({
#             "party_type": "Supplier",
#             "party": doc_supplier,
#             "account": doc.opposite_account_link_a_001,
#             "debit_in_account_currency": 0,
#             "credit_in_account_currency": total_amount,
#         })
#     else:
#         accounts.append({
#             "account": doc.opposite_account_link_a_001,
#             "debit_in_account_currency": 0,
#             "credit_in_account_currency": total_amount,
#         })
#
#     journal_entry = frappe.get_doc({
#         "doctype": "Journal Entry",
#         "voucher_type": "Cash Entry",
#         "posting_date": doc.posting_date,
#         "company": doc.company,
#         "accounts": accounts,
#         "user_remark": "Simulated Virtual Debit Account: Total Debit {} applied virtually.".format(total_amount)
#     })
#
#     journal_entry.insert()
#     frappe.db.commit()
#
#     journal_entry.reload()
#
#     journal_entry.submit()
#
#     return journal_entry.name
#



# ====================  3  ====================





@frappe.whitelist()
def create_journal_entry_from_lcv_on_validate(doc, method):
    if not doc.opposite_account_link_a_001:
        frappe.throw("Opposite Account is required.")

    landed_cost_purchase_receipt = frappe.get_all(
        "Landed Cost Purchase Receipt",
        filters={"parent": doc.name},
        fields=["receipt_document_type", "receipt_document", "supplier", "posting_date", "grand_total"],
    )

    if not landed_cost_purchase_receipt:
        frappe.throw("Landed Cost Purchase Receipt not found.")

    doc_supplier = landed_cost_purchase_receipt[0].get('supplier')
    total_amount = doc.total_taxes_and_charges

    accounts = []


    accounts.append({
        "account": frappe.db.get_value("Account", {"account_type": "Temporary"}, "name") or frappe.throw(
            "Please create a 'Temporary' account type in COA for virtual debit handling."
        ),
        "debit_in_account_currency": total_amount,
        "credit_in_account_currency": 0,
    })

    if "2110 - الدائنين" in doc.opposite_account_link_a_001:
        accounts.append({
            "party_type": "Supplier",
            "party": doc_supplier,
            "account": doc.opposite_account_link_a_001,
            "debit_in_account_currency": 0,
            "credit_in_account_currency": total_amount,
        })
    else:
        accounts.append({
            "account": doc.opposite_account_link_a_001,
            "debit_in_account_currency": 0,
            "credit_in_account_currency": total_amount,
        })

    journal_entry = frappe.get_doc({
        "doctype": "Journal Entry",
        "voucher_type": "Cash Entry",
        "posting_date": doc.posting_date,
        "company": doc.company,
        "accounts": accounts,
        "user_remark": "Simulated Virtual Debit Account: Total Debit {} applied virtually.".format(total_amount)
    })

    journal_entry.insert()
    frappe.db.commit()

    journal_entry.reload()

    # journal_entry.submit()

    return journal_entry.name



# ---------------------------------------------------------
# --------------    =============  ---------------





















# ==============================================================
# ==============================================================
# ==============================================================







