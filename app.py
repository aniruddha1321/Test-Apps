"""
Hospital Management Demo Application (Legacy 2018 System)
Run this script to see the legacy system in action.
"""

import sys

BANNER = """
=============================================================
  HOSPITAL EHR MANAGEMENT SYSTEM (LEGACY BUILD v1.4)
  Target for CodeRenew AI Modernization & Security Scanning
=============================================================
"""

def main():
    print(BANNER)
    print("Files in this legacy project:")
    print("  1. patient_records.py  -> Python 2 syntax, HIPAA (plaintext SSN), SQL Injection")
    print("  2. billing_service.py  -> Python 2 syntax, ISO 27001 (credit card logging), hardcoded API key")
    print("  3. legacy_auth.py      -> Weak token generation, hardcoded JWT secret")
    print("  4. PatientPortal.java  -> Java 7 raw types, SQL Injection, Java-to-Python conversion demo")
    print("\nReady for live demonstration in CodeRenew!")

if __name__ == "__main__":
    main()
