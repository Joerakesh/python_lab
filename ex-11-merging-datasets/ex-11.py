# Combining and Merging Datasets
# Course: Python for Data Science | Loyola College, Chennai
# Student: Joe Rakesh A | Department No.: 26-PDS-002

# Exercise 11 — Combining and Merging Datasets
import pandas as pd

customers = pd.DataFrame({
    "cust_id": [1, 2, 3, 4],
    "name": ["Aman", "Bela", "Chirag", "Divya"],
    "city": ["Chennai", "Mumbai", "Delhi", "Pune"],
})
transactions = pd.DataFrame({
    "txn_id": [101, 102, 103, 104, 105],
    "cust_id": [1, 2, 1, 3, 5],
    "product_id": ["P1", "P2", "P1", "P3", "P2"],
    "amount": [500, 1200, 300, 750, 900],
})
products = pd.DataFrame({
    "product_id": ["P1", "P2", "P3"],
    "product_name": ["Laptop Bag", "Wireless Mouse", "Keyboard"],
    "category": ["Accessories", "Accessories", "Peripherals"],
})

merged = transactions.merge(customers, on="cust_id", how="left", indicator=True)
print("Transactions merged with Customers (left join, with indicator):\n", merged)
full = merged.merge(products, on="product_id", how="left")
print("\nFully merged dataset (transactions + customers + products):\n", full)
unmatched = merged[merged["_merge"] == "left_only"]
print("\nTransactions with no matching customer record:\n", unmatched[["txn_id", "cust_id", "amount"]])
revenue_by_city = full.groupby("city", dropna=True)["amount"].sum().sort_values(ascending=False)
print("\nRevenue by city:\n", revenue_by_city)
