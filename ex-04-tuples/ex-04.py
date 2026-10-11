# Creating and Manipulating Tuple
# Course: Python for Data Science | Loyola College, Chennai
# Student: Joe Rakesh A | Department No.: 26-PDS-002

# Exercise 04 — Creating and Manipulating Tuple
from collections import namedtuple
from datetime import datetime

# Foundational tuple operations
coordinates = (10, 20, 30)
print("Tuple:", coordinates)
print("Index 0:", coordinates[0])
print("Slice:", coordinates[:2])
print("Concatenation:", coordinates + (40,))
x, y, z = coordinates
print("Unpacked:", x, y, z)

SensorReading = namedtuple("SensorReading", ["sensor_id", "timestamp", "value", "unit"])
readings = [
    SensorReading("S1", datetime(2026, 1, 1, 8, 0), 23.5, "C"),
    SensorReading("S1", datetime(2026, 1, 1, 9, 0), 24.1, "C"),
    SensorReading("S2", datetime(2026, 1, 1, 8, 0), 98.2, "kPa"),
    SensorReading("S1", datetime(2026, 1, 1, 10, 0), 90.0, "C"),
]
print("\nAll readings:")
for reading in readings:
    print(f" {reading.sensor_id} | {reading.timestamp} | {reading.value} {reading.unit}")
grouped = {}
for reading in readings:
    grouped.setdefault(reading.sensor_id, []).append(reading.value)
print("\nAverage value per sensor:")
for sensor_id, values in grouped.items():
    print(f" {sensor_id}: avg = {sum(values) / len(values):.2f}")
try:
    readings[0].value = 25.0
except AttributeError as error:
    print("\nImmutability check ->", error)
