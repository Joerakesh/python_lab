# Flow Control
# Course: Python for Data Science | Loyola College, Chennai
# Student: Joe Rakesh A | Department No.: 26-PDS-002

# Exercise 01 — Flow Control
# A. Foundational: multiplication table, skipping multiples of 3
n = 7
print("A. Multiplication table (multiples of 3 skipped):")
for i in range(1, 11):
    if i % 3 == 0:
        print("skip")
    else:
        print(f"{n} x {i} = {n * i}")

# B. Applied: grade frequency without Counter
scores = [95, 82, 74, 68, 55, 43, 31, 90, 76, 61]
grades = {"A": 0, "B": 0, "C": 0, "D": 0, "F": 0}
for score in scores:
    if score >= 90:
        grades["A"] += 1
    elif score >= 75:
        grades["B"] += 1
    elif score >= 60:
        grades["C"] += 1
    elif score >= 40:
        grades["D"] += 1
    else:
        grades["F"] += 1
print("\nB. Grade counts:")
for grade, count in grades.items():
    print(f"{grade}: {count}")

# C. Advanced: manual population mean, standard deviation and z-scores
data = [12, 15, 14, 10, 13, 200, 11, 9, 16, 14, -50, 12, 15]
count = len(data)
mean = sum(data) / count
variance_sum = 0
for value in data:
    variance_sum += (value - mean) ** 2
std_dev = (variance_sum / count) ** 0.5
threshold = 2
outliers = []
for value in data:
    z_score = (value - mean) / std_dev if std_dev else 0.0
    if abs(z_score) > threshold:
        outliers.append((value, round(z_score, 2)))
print("\nC. Manual outlier detection:")
print("Dataset:", data)
print(f"Mean: {mean:.2f}, Std Dev: {std_dev:.2f}")
print(f"Outliers (|z| > {threshold}):", outliers)
print(f"Total records: {count}, outliers found: {len(outliers)} ({len(outliers)/count*100:.1f}%)")
