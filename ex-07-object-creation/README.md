# Exercise 07 — Object Creation and Usage

**Course:** Python for Data Science  
**Programme:** I M.Sc. Data Science · I Semester  
**Department Number:** 26-PDS-002  
**Student:** Joe Rakesh A · Loyola College, Chennai  
**Date in practical record:** 24-07-2026

## 1. Aim

Implement a StandardScaler-style class with fit, transform, fit_transform and inverse_transform methods, fitting statistics on training data only.

## 2. Algorithm

1. Define the scaler class and initialize its learned state.
2. Compute mean and population standard deviation in fit().
3. Use learned training statistics in transform().
4. Implement fit_transform() and inverse_transform().
5. Scale unseen test values with training statistics and verify restoration.

## 3. Implementation

- [Python program](./ex-07.py)
- [Executable Jupyter notebook](./ex-07.ipynb)

The notebook contains the same runnable program. Execute it from top to bottom to regenerate outputs.

## 4. Recorded reference output

The practical record reports mean 60.71 and standard deviation 11.16; test values [58, 90] scale to approximately [-0.243, 2.625], and inverse-transform restores the training values.

This summary is based on the supplied practical record; it is not presented as a fresh execution result. Some printed lines in the scanned PDF are incomplete or garbled.

## 5. Conclusion

Implement a StandardScaler-style class with fit, transform, fit_transform and inverse_transform methods, fitting statistics on training data only. The program is designed to display the relevant results and demonstrate the concepts specified in the practical record. Verify generated notebook output after execution.

## 6. Reproducibility

- Python: GitHub Actions uses Python 3.12.
- Dataset source: inline example data; no external dataset file is required.
- Dependencies: built-in Python modules unless otherwise imported.
- Run locally: `python ex-07.py`.
- Environment snapshot: `python --version` and `python -m pip freeze`.
