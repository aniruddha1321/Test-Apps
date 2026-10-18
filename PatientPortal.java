package com.hospital.portal;

import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.ResultSet;
import java.sql.Statement;
import java.util.ArrayList;
import java.util.Vector;

/**
 * PatientPortal - Legacy Java 7 Hospital Portal Backend
 * Contains raw types, hardcoded credentials, and SQL injection vulnerability.
 */
public class PatientPortal {

    // Hardcoded Database Credentials (ISO 27001 Violation)
    private static final String DB_URL = "jdbc:mysql://10.0.0.45:3306/hospital_ehr";
    private static final String DB_USER = "portal_user";
    private static final String DB_PASS = "HospitalAdmin2015!";

    public static void main(String[] args) {
        System.out.println("Starting Hospital Patient Portal (Java 7)...");
        PatientPortal portal = new PatientPortal();
        portal.getPatientDetails("P001");
    }

    /**
     * Fetch patient details by ID.
     * VULNERABILITY: SQL Injection via unescaped string concatenation.
     */
    public ArrayList getPatientDetails(String patientId) {
        // Legacy raw types without generics
        ArrayList results = new ArrayList();
        Vector legacyVector = new Vector();

        Connection conn = null;
        Statement stmt = null;
        ResultSet rs = null;

        try {
            conn = DriverManager.getConnection(DB_URL, DB_USER, DB_PASS);
            stmt = conn.createStatement();

            // SQL INJECTION: Unsanitized concatenation
            String sql = "SELECT id, name, ssn, diagnosis FROM patients WHERE id = '" + patientId + "'";
            System.out.println("Executing query: " + sql);

            rs = stmt.executeQuery(sql);

            while (rs.next()) {
                String record = "Patient: " + rs.getString("name") +
                                ", SSN: " + rs.getString("ssn") +
                                ", Diagnosis: " + rs.getString("diagnosis");
                results.add(record);
                legacyVector.add(record);
            }
        } catch (Exception e) {
            e.printStackTrace();
        } finally {
            try {
                if (rs != null) rs.close();
                if (stmt != null) stmt.close();
                if (conn != null) conn.close();
            } catch (Exception ex) {
                ex.printStackTrace();
            }
        }

        return results;
    }
}
