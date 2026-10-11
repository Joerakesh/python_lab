# Exercise 04 — Creating and Manipulating Tuple

**Course:** Python for Data Science  
**Programme:** I M.Sc. Data Science · I Semester  
**Department Number:** 26-PDS-002  
**Student:** Joe Rakesh A · Loyola College, Chennai  
**Date in practical record:** 10-07-2026

## 1. Aim

Create and manipulate tuples and use immutable named records to group and summarize structured sensor readings.

## 2. Algorithm

1. Define a namedtuple schema for sensor ID, timestamp, value and unit.
2. Create sensor records and display their attributes.
3. Group measurements by sensor ID.
4. Calculate the average value per sensor.
5. Attempt to modify a namedtuple field and show the immutability error.

## 3. Implementation

- [Python program](./ex-04.py)
- [Executable Jupyter notebook](./ex-04.ipynb)

The notebook contains the same runnable program. Execute it from top to bottom to regenerate outputs.

## 4. Recorded reference output

The practical record reports S1 average 45.87, S2 average 98.20 and an immutability error ('can't set attribute').

This summary is based on the supplied practical record; it is not presented as a fresh execution result. Some output rows in the scanned PDF are garbled or incomplete.

## 5. Conclusion

Create and manipulate tuples and use immutable named records to group and summarize structured sensor readings. The program is designed to display the relevant results and demonstrate the concepts specified in the practical record. Verify the generated notebook output after execution.

## 6. Reproducibility

- Python: GitHub Actions uses Python 3.12.
- External data files: none required for this exercise.
- Dependencies: built-in Python modules unless the script explicitly imports an external package.
- Run locally: `python ex-04.py`.
- For an environment snapshot: `python --version` and `python -m pip freeze`.
