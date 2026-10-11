# Data Aggregation and Group-wise Operations
# Course: Python for Data Science | Loyola College, Chennai
# Student: Joe Rakesh A | Department No.: 26-PDS-002

# Exercise 13 — Data Aggregation and Group-wise Operations
import pandas as pd

pd.set_option("display.width", 120)
sales = pd.DataFrame({
    "Region": ["East", "West", "East", "South", "West", "South", "East", "West"],
    "Product": ["A", "B", "A", "C", "A", "B", "C", "C"],
    "Quantity": [10, 15, 8, 20, 12, 5, 18, 9],
    "Revenue": [1000, 1800, 800, 2500, 1400, 600, 2200, 950],
})

agg_result = sales.groupby("Region").agg(
    Total_Revenue=("Revenue", "sum"),
    Avg_Revenue=("Revenue", "mean"),
    Revenue_CV=("Revenue", lambda values: values.std() / values.mean() if values.mean() else 0),
)
print("Custom aggregation (sum, mean, coefficient of variation) by Region:\n", agg_result)

pivot = pd.pivot_table(
    sales, values="Revenue", index="Region", columns="Product", aggfunc="sum", fill_value=0
)
print("\nPivot table (Revenue by Region x Product):\n", pivot)

sales["Revenue_Share_in_Region"] = sales.groupby("Region")["Revenue"].transform(
    lambda values: values / values.sum()
)
print("\nRow-level share of regional revenue (via transform):\n",
      sales[["Region", "Product", "Revenue", "Revenue_Share_in_Region"]])
