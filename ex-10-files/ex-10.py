# Reading and Writing Text and Binary Files
# Course: Python for Data Science | Loyola College, Chennai
# Student: Joe Rakesh A | Department No.: 26-PDS-002

# Exercise 10 — Reading and Writing Text and Binary Files
import csv
import json
import pickle
from pathlib import Path

output_dir = Path("python_lab_output")
output_dir.mkdir(exist_ok=True)
csv_path = output_dir / "scores.csv"
json_path = output_dir / "scores_clean.json"
pickle_path = output_dir / "model.pkl"

rows = [
    ["id", "name", "score"],
    ["1", "Aman", "85"],
    ["2", "Bela", "NA"],
    ["3", "Chirag", "92"],
]
with csv_path.open("w", newline="", encoding="utf-8") as file:
    csv.writer(file).writerows(rows)

cleaned = []
with csv_path.open("r", newline="", encoding="utf-8") as file:
    for row in csv.DictReader(file):
        score = row["score"]
        row["score"] = None if score == "NA" else int(score)
        cleaned.append(row)

valid_scores = [row["score"] for row in cleaned if row["score"] is not None]
print("Cleaned records from CSV:")
for record in cleaned:
    print(" ", record)
print(f"\nAverage score (ignoring missing): {sum(valid_scores)/len(valid_scores):.2f}")

with json_path.open("w", encoding="utf-8") as file:
    json.dump(cleaned, file, indent=2)
with json_path.open("r", encoding="utf-8") as file:
    print("\nJSON file content:")
    print(file.read())

model_coeffs = {"slope": 1.5, "intercept": 0.3, "features": ["score"]}
with pickle_path.open("wb") as file:
    pickle.dump(model_coeffs, file)
with pickle_path.open("rb") as file:
    loaded_model = pickle.load(file)
print("Model loaded from binary (pickle) file:", loaded_model)
