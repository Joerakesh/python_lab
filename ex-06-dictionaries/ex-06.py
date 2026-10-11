# Creating and Manipulating a Dictionary
# Course: Python for Data Science | Loyola College, Chennai
# Student: Joe Rakesh A | Department No.: 26-PDS-002

# Exercise 06 — Creating and Manipulating a Dictionary
records = [
    {"id": 1, "dept": "Sales", "region": "East", "revenue": 12000},
    {"id": 2, "dept": "Sales", "region": "West", "revenue": 15000},
    {"id": 3, "dept": "Engineering", "region": "East", "revenue": 22000},
    {"id": 4, "dept": "Sales", "region": "East", "revenue": 9000},
    {"id": 5, "dept": "Engineering", "region": "West", "revenue": 18000},
]
print("Raw nested records:")
for record in records:
    print(record)

summary = {}
for record in records:
    department = record["dept"]
    if department not in summary:
        summary[department] = {"count": 0, "total_revenue": 0, "regions": set()}
    summary[department]["count"] += 1
    summary[department]["total_revenue"] += record["revenue"]
    summary[department]["regions"].add(record["region"])

print("\nDepartment-wise summary:")
for department, values in summary.items():
    average = values["total_revenue"] / values["count"]
    regions = sorted(values["regions"])
    print(f"{department}: count={values['count']}, total_revenue={values['total_revenue']}, "
          f"avg_revenue={average:.2f}, regions={regions}")

categories = ["Accessories", "Peripherals", "Accessories", "Furniture", "Accessories"]
frequency = {}
for category in categories:
    frequency[category] = frequency.get(category, 0) + 1
print("\nCategory frequency:", frequency)
