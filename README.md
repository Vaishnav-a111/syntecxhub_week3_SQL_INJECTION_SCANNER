# SQL Injection Scanner

## Overview
This project is a Python-based SQL Injection vulnerability scanner developed for cybersecurity learning and ethical testing.

The scanner injects SQL payloads into URLs and detects common database error patterns that indicate possible SQL Injection vulnerabilities.

---

## Features
- SQL Injection Payload Testing
- Vulnerability Detection
- Report Generation
- Local Flask Test Server
- Ethical Testing Environment

---

## Technologies Used
- Python
- Flask
- Requests Library

---

## Project Structure

Syntecxhub_SQL_Injection_Scanner/
│
├── scanner.py
├── payloads.txt
├── report.txt
├── test_server.py
├── README.md
└── requirements.txt

---

## How To Run

Install dependencies:

pip install -r requirements.txt

Run vulnerable test server:

python test_server.py

Run scanner:

python scanner.py

Use:

http://127.0.0.1:8000/?id=

---

## Disclaimer
This project is created strictly for educational purposes and authorized security testing environments only.
