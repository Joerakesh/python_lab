# Exercise 10 — Reading and Writing Text and Binary Files

**Course:** Python for Data Science  
**Programme:** I M.Sc. Data Science · I Semester  
**Department Number:** 26-PDS-002  
**Student:** Joe Rakesh A · Loyola College, Chennai  
**Date in practical record:** 20-08-2026

## 1. Aim

Read, clean and write CSV records, serialize cleaned records as JSON and save/load a Python object in a binary pickle file.

## 2. Algorithm

1. Prepare sample CSV data with a missing score marked NA.
2. Write and read the data using csv.
3. Convert NA to None and other scores to integers.
4. Compute the mean of valid scores.
5. Write cleaned data to JSON and serialize a model-coefficient dictionary with pickle.

## 3. Implementation

- [Python program](./ex-10.py)
- [Executable Jupyter notebook](./ex-10.ipynb)

The notebook contains the same runnable program. Execute it from top to bottom to regenerate outputs.

## 4. Recorded reference output

The practical record reports cleaned scores 85, None and 92, with an average of 88.50. The pickle round-trip returns {'slope': 1.5, 'intercept': 0.3, 'features': ['score']}.

This summary is based on the supplied practical record; it is not presented as a fresh execution result. Some printed lines in the scanned PDF are incomplete or garbled.

## 5. Conclusion

Read, clean and write CSV records, serialize cleaned records as JSON and save/load a Python object in a binary pickle file. The program is designed to display the relevant results and demonstrate the concepts specified in the practical record. Verify generated notebook output after execution.

## 6. Reproducibility

- Python: GitHub Actions uses Python 3.12.
- Dataset source: inline example data; no external dataset file is required.
- Dependencies: built-in Python modules unless otherwise imported.
- Run locally: `python ex-10.py`.
- Environment snapshot: `python --version` and `python -m pip freeze`.
