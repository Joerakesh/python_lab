# Exercise 08 — Program Involving Inheritance

**Course:** Python for Data Science  
**Programme:** I M.Sc. Data Science · I Semester  
**Department Number:** 26-PDS-002  
**Student:** Joe Rakesh A · Loyola College, Chennai  
**Date in practical record:** 28-07-2026

## 1. Aim

Demonstrate inheritance and polymorphism using an abstract estimator, a mean baseline and a least-squares linear regressor.

## 2. Algorithm

1. Define an abstract Estimator class with fit() and predict().
2. Implement an MSE score method.
3. Implement MeanRegressor using the training-target mean.
4. Implement LinearRegressor with closed-form least squares.
5. Fit and compare predictions and MSE.

## 3. Implementation

- [Python program](./ex-08.py)
- [Executable Jupyter notebook](./ex-08.ipynb)

The notebook contains the same runnable program. Execute it from top to bottom to regenerate outputs.

## 4. Recorded reference output

The practical record reports MeanRegressor MSE=4.560 and LinearRegressor predictions [2.8, 4.3, 5.8, 7.3, 8.8] with MSE=0.060.

This summary is based on the supplied practical record; it is not presented as a fresh execution result. Some printed lines in the scanned PDF are incomplete or garbled.

## 5. Conclusion

Demonstrate inheritance and polymorphism using an abstract estimator, a mean baseline and a least-squares linear regressor. The program is designed to display the relevant results and demonstrate the concepts specified in the practical record. Verify generated notebook output after execution.

## 6. Reproducibility

- Python: GitHub Actions uses Python 3.12.
- Dataset source: inline example data; no external dataset file is required.
- Dependencies: built-in Python modules unless otherwise imported.
- Run locally: `python ex-08.py`.
- Environment snapshot: `python --version` and `python -m pip freeze`.
