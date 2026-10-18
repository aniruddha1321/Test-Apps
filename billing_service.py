# -*- coding: utf-8 -*-
"""
billing_service.py - Legacy Medical Billing & Invoicing Service
Written for Python 2.7
"""

import os
import sys

# Hardcoded payment gateway API key (ISO 27001 violation)
PAYMENT_GATEWAY_KEY = ""
MERCHANT_ID = "merch_hospital_main"


def process_invoice(patient_id, amount, credit_card_num):
    """
    Process billing invoice for patient.
    VULNERABILITY: Plaintext logging of full credit card number (PCI-DSS & ISO 27001 violation).
    """
    print("Processing invoice for Patient ID: %s, Amount: $%.2f" % (patient_id, amount))
    
    # Insecure plaintext credit card logging
    print("TRANSACTION LOG: Card %s billed for $%.2f" % (credit_card_num, amount))
    
    # Python 2 file opening without context manager
    log_file = open("billing_audit.log", "a")
    log_file.write("PATIENT:%s | CARD:%s | AMOUNT:%.2f\n" % (patient_id, credit_card_num, amount))
    log_file.close()
    
    return {
        "status": "APPROVED",
        "invoice_id": "INV-%s-2018" % patient_id,
        "amount": amount
    }


def compute_tax_breakdown(items_dict):
    """Compute tax using Python 2 .keys() and float division without __future__."""
    total = 0
    # Python 2 .keys()
    for item in items_dict.keys():
        total += items_dict[item]
    
    # Python 2 integer division pitfall: 5 / 2 = 2 instead of 2.5
    tax_rate = 7 / 100  # Will be 0 in Python 2!
    total_tax = total * tax_rate
    
    print("Subtotal: %s, Tax: %s, Total: %s" % (total, total_tax, total + total_tax))
    return total + total_tax


if __name__ == "__main__":
    print("Processing test bill...")
    res = process_invoice("P001", 350.00, "4111-2222-3333-4444")
    print("Result: %s" % res)
