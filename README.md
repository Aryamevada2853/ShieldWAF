# ShieldWAF – Web Application Firewall Prototype

**A Python and Flask-based web application security project for detecting suspicious HTTP requests and monitoring potential web attacks.**

ShieldWAF is a web application security prototype designed to inspect incoming requests, identify configured malicious payload patterns, and notify administrators about potentially suspicious activity.

The project explores fundamental Web Application Firewall (WAF) concepts, including request inspection, pattern-based detection, IP filtering, security logging, and real-time notifications.

---

## Project Overview

Web applications are frequently targeted by attacks such as SQL Injection (SQLi), Cross-Site Scripting (XSS), and Directory Traversal.

ShieldWAF demonstrates a lightweight approach to identifying suspicious request data using configurable detection patterns and Flask-based request handling.

### Key Features

- **SQL Injection Detection:** Identifies configured SQL injection payload patterns.
- **Cross-Site Scripting Detection:** Inspects request data for configured XSS patterns.
- **Directory Traversal Detection:** Checks for configured directory traversal payloads.
- **IP-Based Filtering:** Supports checking requests against a configurable set of blocked IP addresses.
- **Request Monitoring:** Inspects selected application requests.
- **Security Logging:** Records detected malicious requests and valid request activity.
- **Telegram Notifications:** Sends alerts when potentially malicious requests are detected.
- **Web Interface:** Provides a Flask-powered website with an administrative login page.

---

## Technology Stack

| Technology | Purpose |
|---|---|
| Python | Backend development |
| Flask | Web application framework |
| HTML5 | Frontend structure |
| CSS3 | Website styling |
| Bootstrap | Responsive UI |
| JavaScript | Frontend functionality |
| Regular Expressions | Pattern-based payload detection |
| SQLite | Listed in the original project requirements; verify actual implementation before claiming database integration |
| Telegram Bot API | Security notifications |
| Python Logging | Security event logging |

---

## Architecture

ShieldWAF follows a simple request-inspection workflow.

```text
             Incoming HTTP Request
                      |
                      v
               Flask Application
                      |
                      v
                Request Inspection
                      |
             +--------+--------+
             |                 |
             v                 v
        IP Filtering     Payload Inspection
                               |
                               v
                      Pattern-Based Detection
                               |
                     +---------+---------+
                     |                   |
                     v                   v
                Suspicious             Normal
                  Request              Request
                     |                   |
                     v                   v
               Security Log        Activity Log
                     |
                     v
              Telegram Alert
```

---

## Project Structure

```text
ShieldWAF/
│
├── waf.py
├── malicious_payload.txt
├── README.md
├── requirements.txt
├── .env.example
├── .gitignore
│
├── templates/
│   ├── index.html
│   ├── login.html
│   ├── about.html
│   ├── contact.html
│   ├── service.html
│   ├── why.html
│   ├── team.html
│   └── 403.html
│
└── static/
    ├── css/
    ├── js/
    └── images/
```

---

## Installation and Setup

### 1. Clone the Repository

```bash
git clone https://github.com/YOUR_USERNAME/ShieldWAF.git
cd ShieldWAF
```

### 2. Create a Virtual Environment

Windows:

```powershell
python -m venv venv
.\venv\Scripts\Activate.ps1
```

Linux / macOS:

```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure Environment Variables

Copy `.env.example` to `.env` and configure your local secrets.

Never commit `.env` or expose Telegram bot tokens, API keys, or administrator credentials.

The application code must read these values from environment variables before using this configuration.

### 5. Run the Application

```bash
python waf.py
```

Open your browser:

```text
http://127.0.0.1:5555/
```

---

## Security Testing

ShieldWAF can be tested using a controlled local environment.

Suggested test cases:

| Test Case | Purpose |
|---|---|
| Normal HTTP request | Check normal request handling |
| SQL Injection payload | Test configured SQLi signatures |
| XSS payload | Test configured XSS signatures |
| Directory Traversal payload | Test configured traversal signatures |
| Blocked IP address | Test IP-based filtering |
| Telegram notification | Verify security alert delivery |

### Example XSS Test

Use a controlled local test environment and submit a harmless XSS test string through a form.

```html
<script>alert(1)</script>
```

Observe whether the configured detection pattern identifies the request, records the event, and triggers the Telegram notification.

**Note:** Detection depends on the signatures configured in `malicious_payload.txt`. A successful test does not establish complete XSS protection.

---

## Current Limitations

ShieldWAF is an educational security prototype, not a production-ready WAF.

Known limitations include:

- Pattern-based detection can produce false positives and false negatives.
- Attack detection depends on manually configured payload signatures.
- Only selected application routes are inspected.
- IP filtering currently uses an in-memory data structure.
- Detection patterns do not cover every encoding or obfuscation technique.
- Production-grade authentication, rate limiting, and request normalization require further development.
- Scalability and performance require additional evaluation.

---

## Future Improvements

Potential areas for further development:

- Advanced request normalization and canonicalization.
- Improved SQLi, XSS and directory traversal detection.
- Automated security testing with pytest.
- Authentication hardening and role-based access control.
- Rate limiting and abuse prevention.
- Structured security event monitoring.
- Docker-based deployment.
- Performance benchmarking and detection evaluation.
- Integration with additional security monitoring tools.

---

## Skills Demonstrated

This project explores practical concepts relevant to:

- Web Application Security
- OWASP Top 10
- HTTP Request Inspection
- SQL Injection and XSS Detection
- Regular Expression-Based Detection
- Python and Flask Development
- Security Logging and Monitoring
- API Integration
- Basic WAF Architecture

---

## Disclaimer

ShieldWAF is an educational and experimental project intended for security research and testing in controlled environments.

It should not be deployed as the sole security control protecting a production application.

---

## Author

**Arya Mevada**

M.Sc. Cybersecurity Student  
Saarland University, Germany

Interests: Application Security | Web Penetration Testing | Vulnerability Assessment | Cybersecurity Research

---

**If you find this project interesting, feel free to explore the code and contribute improvements.**