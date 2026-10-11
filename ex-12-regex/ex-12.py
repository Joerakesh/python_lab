# Program Involving Regular Expressions
# Course: Python for Data Science | Loyola College, Chennai
# Student: Joe Rakesh A | Department No.: 26-PDS-002

# Exercise 12 — Program Involving Regular Expressions
import re
from datetime import datetime

raw_records = [
    "Name: Aman Kumar | Phone: +91-98765-43210 | Email: aman.kumar@company.com | Joined: 2023-05-14",
    "Name: Bela Rao | Phone: 9876543210 | Email: bela_rao123@mail.co.in | Joined: 14/06/2022",
    "Name: Chirag Shah | Phone: (98)76543211 | Email: chirag@dept.org | Joined: 2021.11.02",
]
pattern = re.compile(
    r"Name:\s*(?P<name>[A-Za-z ]+)\s*\|\s*"
    r"Phone:\s*(?P<phone>[\d()+\- ]+)\s*\|\s*"
    r"Email:\s*(?P<email>[\w.+-]+@[\w.-]+)\s*\|\s*"
    r"Joined:\s*(?P<joined>[\d./-]+)"
)

def normalize_phone(phone):
    digits = re.sub(r"\D", "", phone)
    return digits[-10:]

def normalize_date(date_text):
    for fmt in ("%Y-%m-%d", "%d/%m/%Y", "%Y.%m.%d", "%d-%m-%Y"):
        try:
            return datetime.strptime(date_text, fmt).strftime("%Y-%m-%d")
        except ValueError:
            continue
    raise ValueError(f"Unsupported date format: {date_text}")

print("Cleaned records:")
for line in raw_records:
    match = pattern.search(line)
    if not match:
        print(" No match:", line)
        continue
    groups = match.groupdict()
    cleaned = {
        "name": groups["name"].strip(),
        "phone": normalize_phone(groups["phone"]),
        "email": groups["email"].lower(),
        "joined": normalize_date(groups["joined"]),
    }
    print(" ", cleaned)
