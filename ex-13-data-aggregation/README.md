# Exercise 13 — Data Aggregation and Group-wise Operations

**Course:** Python for Data Science  
**Programme:** I M.Sc. Data Science · I Semester  
**Department Number:** 26-PDS-002  
**Student:** Joe Rakesh A · Loyola College, Chennai  
**Date in practical record:** 22-09-2026

## 1. Aim

Use pandas groupby aggregations, custom coefficient-of-variation aggregation, pivot tables and group-wise transform for revenue analysis.

## 2. Algorithm

1. Create a sales DataFrame with region, product, quantity and revenue.
2. Group by region and calculate total revenue, mean revenue and coefficient of variation.
3. Create a Region × Product pivot table.
4. Use groupby().transform() to compute each row's share of regional revenue.
5. Display summaries and transformed row-level values.

## 3. Implementation

- [Python program](./ex-13.py)
- [Executable Jupyter notebook](./ex-13.ipynb)

## 4. Recorded reference output

The practical record reports regional total revenues East=4000, South=3100 and West=4150. The row-level regional revenue shares are printed in the record; executing the notebook regenerates the complete summary tables.

This is transcribed from the supplied practical record and is not presented as a fresh execution result.

## 5. Conclusion

The exercise demonstrates group-wise aggregation, custom statistics, pivot tables and row-level transformations using pandas. Inspect the generated table to compare total revenue by region and check that each row's regional revenue share sums to 1 within each region.

## 6. Reproducibility

- Python: GitHub Actions uses Python 3.12.
- Dataset: inline example data; no external dataset file is required.
- Dependency: pandas (listed in `requirements.txt`).
- Run locally: `python ex-13.py`.
- Environment snapshot: `python --version` and `python -m pip freeze`.
