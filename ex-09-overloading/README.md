# Exercise 09 — Program Involving Overloading

**Course:** Python for Data Science  
**Programme:** I M.Sc. Data Science · I Semester  
**Department Number:** 26-PDS-002  
**Student:** Joe Rakesh A · Loyola College, Chennai  
**Date in practical record:** 06-08-2026

## 1. Aim

Demonstrate operator overloading in a Matrix class with shape validation, element-wise addition and matrix multiplication.

## 2. Algorithm

1. Create a Matrix class storing data and dimensions.
2. Overload __add__ and validate equal dimensions.
3. Overload __mul__ and check compatible dimensions.
4. Calculate product entries using dot products.
5. Implement __repr__ and display the matrices and results.

## 3. Implementation

- [Python program](./ex-09.py)
- [Executable Jupyter notebook](./ex-09.ipynb)

The notebook contains the same runnable program. Execute it from top to bottom to regenerate outputs.

## 4. Recorded reference output

The practical record reports A+B=[[6, 8], [10, 12]] and A*B=[[19, 22], [43, 50]].

This summary is based on the supplied practical record; it is not presented as a fresh execution result. Some printed lines in the scanned PDF are incomplete or garbled.

## 5. Conclusion

Demonstrate operator overloading in a Matrix class with shape validation, element-wise addition and matrix multiplication. The program is designed to display the relevant results and demonstrate the concepts specified in the practical record. Verify generated notebook output after execution.

## 6. Reproducibility

- Python: GitHub Actions uses Python 3.12.
- Dataset source: inline example data; no external dataset file is required.
- Dependencies: built-in Python modules unless otherwise imported.
- Run locally: `python ex-09.py`.
- Environment snapshot: `python --version` and `python -m pip freeze`.
