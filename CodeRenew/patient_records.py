# -*- coding: utf-8 -*-
"""
patient_records.py - Legacy Hospital Patient Records System
Written for Python 2.7 (Legacy Codebase)
WARNING: Contains intentional Python 2 syntax and security flaws for CodeRenew demonstration.
"""

import sys
import hashlib
import urllib2

# Hardcoded credentials (Security / ISO 27001 violation)
DB_HOST = "10.0.0.45"
DB_USER = "hospital_admin"
DB_PASSWORD = "HardcodedSuperSecret2018!"
DATABASE_NAME = "hospital_ehr_db"

# In-memory patient store (Python 2 style)
_PATIENTS_DB = {
    "P001": {
        "name": "Jane Doe",
        "ssn": "987-65-4321",         # HIPAA Violation: Plaintext unencrypted SSN
        "diagnosis": "Type 2 Diabetes", # HIPAA Violation: Unencrypted PHI
        "password_hash": hashlib.md5("patient123").hexdigest(), # ISO 27001: Weak MD5 hash
        "active": True
    },
    "P002": {
        "name": "John Smith",
        "ssn": "123-45-6789",
        "diagnosis": "Hypertension",
        "password_hash": hashlib.md5("secret456").hexdigest(),
        "active": False
    }
}


def lookup_patient(patient_id):
    """Lookup patient by ID using Python 2 dictionary methods."""
    print "Looking up patient records for ID: %s" % patient_id
    
    # Python 2 specific method: .has_key()
    if _PATIENTS_DB.has_key(patient_id):
        patient = _PATIENTS_DB[patient_id]
        print "Found record for %s" % patient["name"]
        return patient
    else:
        print >> sys.stderr, "Error: Patient %s not found." % patient_id
        return None


def execute_patient_search_query(db_connection, ssn_input):
    """
    Search database for patient by SSN.
    VULNERABILITY: SQL Injection through raw string formatting.
    """
    # Direct string formatting in SQL query -> SQL Injection vulnerability
    query = "SELECT * FROM patients WHERE ssn = '%s' AND active = 1" % ssn_input
    print "Executing database query: %s" % query
    
    try:
        cursor = db_connection.cursor()
        cursor.execute(query)
        return cursor.fetchall()
    except Exception, exc:  # Python 2 comma exception syntax
        print "Query execution failed: %s" % str(exc)
        return None


def calculate_risk_scores(patient_ids):
    """Calculate patient risk using Python 2 xrange and iteritems."""
    scores = {}
    print "Calculating risk scores across %d records..." % len(patient_ids)
    
    # Python 2 xrange
    for i in xrange(len(patient_ids)):
        pid = patient_ids[i]
        scores[pid] = (i + 1) * 15.5
    
    # Python 2 .iteritems()
    for pid, score in scores.iteritems():
        print "Patient: %s -> Risk Score: %.2f" % (pid, score)
        
    return scores


def fetch_external_records(endpoint_url):
    """Fetch external EHR data using deprecated urllib2."""
    try:
        req = urllib2.Request(endpoint_url)
        response = urllib2.urlopen(req, timeout=5)
        raw_html = response.read()
        return raw_html
    except urllib2.URLError, err:  # Python 2 comma syntax
        print "Failed to fetch external records: %s" % err.reason
        return None


if __name__ == "__main__":
    print "=== Legacy Patient Records System (Python 2.7) ==="
    p = lookup_patient("P001")
    if p:
        print "Patient Name: %s, SSN: %s" % (p["name"], p["ssn"])
    calculate_risk_scores(["P001", "P002"])
