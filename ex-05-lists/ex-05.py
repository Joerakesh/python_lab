# Creating and Manipulating a List
# Course: Python for Data Science | Loyola College, Chennai
# Student: Joe Rakesh A | Department No.: 26-PDS-002

# Exercise 05 — Creating and Manipulating a List
data = [45, 32, 78, 90, 12, 65, 55, 23]
print("Original data:", data)
data_demo = data.copy()
data_demo.append(100)
data_demo.remove(100)
data_demo.sort()
print("Sorted copy:", data_demo)
print("First three values:", data[:3])

lo, hi = min(data), max(data)
minmax_scaled = [round((x - lo) / (hi - lo), 3) for x in data]
mean = sum(data) / len(data)
std = (sum((x - mean) ** 2 for x in data) / len(data)) ** 0.5
zscore_scaled = [round((x - mean) / std, 3) for x in data]
feature_matrix = [[raw, mm, z] for raw, mm, z in zip(data, minmax_scaled, zscore_scaled)]
print("Min-Max scaled:", minmax_scaled)
print("Z-score scaled:", zscore_scaled)
print("\nFeature Matrix [raw, minmax, zscore]:")
for row in feature_matrix:
    print(row)
print(f"Verification -> Min-Max range: [{min(minmax_scaled)}, {max(minmax_scaled)}]")
print(f"Verification -> Z-score mean ~ {sum(zscore_scaled)/len(zscore_scaled):.3f} (should be ~0)")
