# Exercise 11 — Combining and Merging Datasets

**Course:** Python for Data Science  
**Programme:** I M.Sc. Data Science · I Semester  
**Department Number:** 26-PDS-002  
**Student:** Joe Rakesh A · Loyola College, Chennai  
**Date in practical record:** 28-08-2026

## 1. Aim

Merge customer, transaction and product tables, identify unmatched customer transactions and summarize revenue by city.

## 2. Algorithm

1. Create customer, transaction and product DataFrames.
2. Left-join transactions with customers using indicator=True.
3. Identify unmatched records marked left_only.
4. Join products to the merged transactions.
5. Group by city and sum transaction amounts.

## 3. Implementation

- [Python program](./ex-11.py)
- [Executable Jupyter notebook](./ex-11.ipynb)

The notebook contains the same runnable program. Execute it from top to bottom to regenerate outputs.

## 4. Recorded reference output

The record identifies transaction 105 (cust_id 5, amount 900) as an unmatched customer record. The printed PDF revenue output is incomplete; fresh output from this program should be used.

This summary is based on the supplied practical record; it is not presented as a fresh execution result. Some printed lines in the scanned PDF are incomplete or garbled.

## 5. Conclusion

Merge customer, transaction and product tables, identify unmatched customer transactions and summarize revenue by city. The program is designed to display the relevant results and demonstrate the concepts specified in the practical record. Verify generated notebook output after execution.

## 6. Reproducibility

- Python: GitHub Actions uses Python 3.12.
- Dataset source: inline example data; no external dataset file is required.
- Dependencies: built-in Python modules unless otherwise imported.
- Run locally: `python ex-11.py`.
- Environment snapshot: `python --version` and `python -m pip freeze`.
