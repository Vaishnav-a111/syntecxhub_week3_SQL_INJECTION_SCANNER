import requests
import time

# SQL Error Messages
sql_errors = [
    "sql syntax",
    "mysql",
    "syntax error",
    "warning",
    "database error",
    "mysqli",
    "sqlite",
    "oracle"
]

# Read payloads
with open("payloads.txt", "r") as file:
    payloads = file.read().splitlines()

# Target URL
url = input("Enter Target URL: ")

# Headers
headers = {
    "User-Agent": "Mozilla/5.0"
}

# Report File
report = open("report.txt", "w")

print("\nStarting SQL Injection Scan...\n")

# Scan each payload
for payload in payloads:

    target = url + payload

    try:
        response = requests.get(
            target,
            headers=headers,
            timeout=20
        )

        vulnerable = False

        for error in sql_errors:

            if error.lower() in response.text.lower():

                result = f"[VULNERABLE] {target}"

                print(result)

                report.write(result + "\n")

                vulnerable = True

                break

        if not vulnerable:
            print(f"[SAFE] {target}")

    except Exception as e:
        print(f"[ERROR] {target}")
        print("Reason:", e)

    # Slow down requests
    time.sleep(3)

report.close()

print("\nScan Completed!")
print("Results saved in report.txt")