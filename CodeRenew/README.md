# Hospital EHR System (Legacy Demo Application)

This is a realistic legacy codebase designed specifically to **demonstrate Google Cloud CodeRenew** during presentations, judging, and live demos.

It contains intentional legacy syntax and compliance flaws that highlight CodeRenew's **Vertex AI Gemini 1.5 Pro** capabilities.

---

## Files Included

| File | Language | Purpose in Demonstration |
|---|---|---|
| `patient_records.py` | Python 2.7 | **Python 2 to 3 Modernization** + **HIPAA Violations** (SSN & diagnosis) + **SQL Injection** |
| `billing_service.py` | Python 2.7 | **Python 2 Modernization** + **ISO 27001 Violations** (credit card logging) + Hardcoded API key |
| `legacy_auth.py` | Python 2.7 | **Insecure Random Tokens** + Hardcoded JWT secret |
| `PatientPortal.java` | Java 7 | **Java-to-Python Conversion** + SQL Injection + Raw types |
| `app.py` | Python | Overview script showing system structure |

---

## 4-Step Live Demo Walkthrough

### 🚀 Demo Step 1: Python 2 to 3 Modernization
1. Open your live CodeRenew app: **https://coderenew-backend-1865280733.us-central1.run.app**
2. In the **Code Editor / Modernizer**:
   - Open or paste the code from `patient_records.py`.
   - Select **Python 2 to Python 3 Modernization**.
   - Click **Modernize Code**.
3. **What to show judges**:
   - Vertex AI replaces legacy `print "..."` with `print(...)`.
   - Converts `except Exception, exc:` to `except Exception as exc:`.
   - Converts deprecated `xrange()` and `.has_key()` to modern Python 3 idioms.
   - Adds type annotations, f-strings, and generates a structured explanation of changes.

---

### 🛡️ Demo Step 2: Automated Security & HIPAA / ISO 27001 Audit
1. Go to the **Security Scan** tab in CodeRenew.
2. Upload `patient_records.py` and `billing_service.py`.
3. Click **Scan Files**.
4. **What to show judges**:
   - **HIPAA Violation**: CodeRenew flags unencrypted patient Social Security Numbers and diagnosis fields.
   - **SQL Injection**: Flags line `query = "SELECT * FROM patients WHERE ssn = '%s'" % ssn_input` and provides parameterized query remediation.
   - **ISO 27001 / PCI-DSS**: Flags plaintext credit card number logging and hardcoded credentials (`DB_PASSWORD`, `PAYMENT_GATEWAY_KEY`).

---

### 🔄 Demo Step 3: Multi-Language Java to Python Conversion
1. In the Code Workspace, switch mode to **Java to Python**.
2. Paste the contents of `PatientPortal.java`.
3. Click **Convert**.
4. **What to show judges**:
   - Vertex AI converts Java raw types (`ArrayList`, `Vector`, `Connection`) into clean, idiomatic Python 3 dataclasses and modern database patterns.
   - Resolves Java-specific boilerplate.

---

### 💬 Demo Step 4: Ask the Vertex AI Copilot
1. Open the **CodeRenew AI Assistant** chatbot (bottom right).
2. Ask: *"What are the HIPAA compliance risks in patient_records.py?"* or *"How did you convert the Java SQL query to secure Python?"*
3. Watch Gemini 1.5 Pro explain the remediation in real time.
