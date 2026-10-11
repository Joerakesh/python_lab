# Functions
# Course: Python for Data Science | Loyola College, Chennai
# Student: Joe Rakesh A | Department No.: 26-PDS-002

# Exercise 02 — Functions
import math
import time
from functools import wraps

def factorial(n):
    if n < 0:
        raise ValueError("factorial is undefined for negative integers")
    return 1 if n <= 1 else n * factorial(n - 1)

def fibonacci(n):
    if n < 0:
        raise ValueError("Fibonacci index must be non-negative")
    if n <= 1:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)

def apply_transform(data, func):
    return [func(value) for value in data]

def timer(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start = time.perf_counter()
        result = func(*args, **kwargs)
        elapsed_ms = (time.perf_counter() - start) * 1000
        print(f"[{func.__name__}] executed in {elapsed_ms:.4f} ms")
        return result
    return wrapper

@timer
def scale_feature(data, method="minmax", **kwargs):
    if not data:
        raise ValueError("data must not be empty")
    if method == "minmax":
        lo, hi = min(data), max(data)
        if lo == hi:
            return [0.0 for _ in data]
        return [(x - lo) / (hi - lo) for x in data]
    if method == "zscore":
        mean = sum(data) / len(data)
        std = (sum((x - mean) ** 2 for x in data) / len(data)) ** 0.5
        if std == 0:
            return [0.0 for _ in data]
        return [(x - mean) / std for x in data]
    raise ValueError(f"Unknown scaling method: {method}")

print("Factorial(5):", factorial(5))
print("Fibonacci(7):", fibonacci(7))
values = [1, 4, 9, 16]
print("Square roots:", apply_transform(values, math.sqrt))
features = [10, 20, 15, 40, 25, 30]
print("Original:", features)
print("Min-Max scaled:", [round(x, 3) for x in scale_feature(features, method="minmax")])
print("Z-score scaled:", [round(x, 3) for x in scale_feature(features, method="zscore")])
