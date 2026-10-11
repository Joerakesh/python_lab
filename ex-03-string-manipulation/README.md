# Exercise 03 — String Manipulation

**Course:** Python for Data Science  
**Programme:** I M.Sc. Data Science · I Semester  
**Department Number:** 26-PDS-002  
**Student:** Joe Rakesh A · Loyola College, Chennai  
**Date in practical record:** 07-07-2026

## 1. Aim

Clean text, tokenize with regular expressions, remove stopwords and build a Bag-of-Words frequency summary.

## 2. Algorithm

1. Prepare sample text records.
2. Normalize text by lowercasing and extracting alphabetic tokens.
3. Remove terms in a stopword set.
4. Combine remaining tokens.
5. Count terms and report vocabulary size and total token count.

## 3. Implementation

- [Python program](./ex-03.py)
- [Executable Jupyter notebook](./ex-03.ipynb)

The notebook contains the same runnable program. Execute it from top to bottom to regenerate outputs.

## 4. Recorded reference output

The printed record lists a cleaned Bag-of-Words vocabulary containing data, science, programming, machine, learning, combines, statistics, subset, skills and essential. The PDF text extraction does not preserve all corresponding frequency values clearly.

This summary is based on the supplied practical record; it is not presented as a fresh execution result. Some output rows in the scanned PDF are garbled or incomplete.

## 5. Conclusion

Clean text, tokenize with regular expressions, remove stopwords and build a Bag-of-Words frequency summary. The program is designed to display the relevant results and demonstrate the concepts specified in the practical record. Verify the generated notebook output after execution.

## 6. Reproducibility

- Python: GitHub Actions uses Python 3.12.
- External data files: none required for this exercise.
- Dependencies: built-in Python modules unless the script explicitly imports an external package.
- Run locally: `python ex-03.py`.
- For an environment snapshot: `python --version` and `python -m pip freeze`.
