# Exercise 12 — Program Involving Regular Expressions

**Course:** Python for Data Science  
**Programme:** I M.Sc. Data Science · I Semester  
**Department Number:** 26-PDS-002  
**Student:** Joe Rakesh A · Loyola College, Chennai  
**Date in practical record:** 07-09-2026

## 1. Aim

Use regular expressions with named groups to parse semi-structured text, validate/extract fields, normalize phone numbers and standardize dates.

## 2. Algorithm

1. Prepare records with name, phone, email and joined-date fields.
2. Compile a regular expression with named groups.
3. Extract each field and normalize phone numbers to ten digits.
4. Normalize dates to YYYY-MM-DD.
5. Print cleaned records or report lines that do not match.

## 3. Implementation

- [Python program](./ex-12.py)
- [Executable Jupyter notebook](./ex-12.ipynb)

The notebook contains the same runnable program. Execute it from top to bottom to regenerate outputs.

## 4. Recorded reference output

The record shows three cleaned records; normalized phones are 9876543210, 9876543210 and 9876543211; normalized dates are 2023-05-14, 2022-06-14 and 2021-11-02.

This summary is based on the supplied practical record; it is not presented as a fresh execution result. Some printed lines in the scanned PDF are incomplete or garbled.

## 5. Conclusion

Use regular expressions with named groups to parse semi-structured text, validate/extract fields, normalize phone numbers and standardize dates. The program is designed to display the relevant results and demonstrate the concepts specified in the practical record. Verify generated notebook output after execution.

## 6. Reproducibility

- Python: GitHub Actions uses Python 3.12.
- Dataset source: inline example data; no external dataset file is required.
- Dependencies: built-in Python modules unless otherwise imported.
- Run locally: `python ex-12.py`.
- Environment snapshot: `python --version` and `python -m pip freeze`.
