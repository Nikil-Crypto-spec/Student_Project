#Step 1
#import libraries
import json 
import pandas as pd 
import numpy as np 
import matplotlib.pyplot as plt 
import seaborn as sns

#Step 2
#load dataset
df = pd.read_json("ecommerce_sales.json")
df

#Step 3
#Dataset Exploration
print("\nHEAD")
df.head()

print("\nTAIL")
df.tail()

print("\nSHAPE")
df.shape

print("\nINFO")
df.info()

print("\nDESCRIBE")
df.describe()

print("\nCOLUMNS")
df.columns

print("\nSAMPLE")
df.sample()

print("\nIS NULL")
df.isnull()

print("\nDUPLICATED")
df.duplicated()

#Step 4
#Data Cleaning
print("\nRemove Duplicates")
df.drop_duplicates()

print("\nRemove Missing Values")
df.dropna

print("\nRename columns")
df.rename(columns={
    "Customer_name":"customer_name",
    "Order_ID":"order_id"
})
df.dtypes
print("\nChange datatypes")
df['Price'] = df['Price'].astype(float)
df['Quantity'] = df['Quantity'].astype(int)
df['Discount'] = df['Discount'].astype(float)

#Step 5
#Descriptive Statistics 
print("\nAverage Price")
df["Price"].mean()

print("\nMedian")
df["Price"].median()

print("\nMode")
df["Price"].mode()

print("\nMaximum")
df["Price"].max()

print("\nMinimum")
df["Price"].min()

print("\nVariance")
df["Price"].var()

print("\nStandard Deviation")
df["Price"].std()

print("\nCount")
df["Product"].count()

print("\nUnique Values")
df["Product"].unique()

#Step 6
#Filtering
df[df["Price"] > 50000].value_counts()

df[df["Product"]=="TV"].value_counts()

df[df["State"]=="TS"].value_counts()

df[df["City"]=="Hyderabad"].value_counts()

df[df["Delivery_Status"]=="Shipped"].value_counts()

#Step 7
#Sorting
#ascending
df.sort_values("Price",ascending=True)
df.sort_values("Quantity",ascending=True)

#descending
df.sort_values("Price",ascending=False)
df.sort_values("Quantity",ascending=False)

#Step 8
#Grouping
df.groupby("Category")["Quantity"].sum()

df.groupby("Product")["Price"].sum()

df.groupby("Price")["Discount"].sum()

df.groupby("State")["Price"].sum()

df.groupby("State")["Price"].median()

df.groupby("City")["Price"].sum()

df.groupby("Product")["Price"].mean()

#Step 9
#Aggregation 
#Sum
df.groupby("Product")["Price"].sum()
#mean
df.groupby("Product")["Price"].mean()
#max
df.groupby("Product")["Price"].max()
#min
df.groupby("Product")["Price"].min()
#Count
df.groupby("Product")["Price"].count()
#agg
df.groupby("Product").agg({
    "Price":["min","max","sum"],
     "Discount":["min","max"]
})

df.columns
#Step 10
#Visualization
#Histogram
sns.histplot(
    data=df,
    x="Price",
    bins=12,
    kde=True
)

plt.title("Price Distribution")
plt.show()

#Bar chart
sns.barplot(
    data=df,
    x="Product",
    y="Price"
)

plt.title("Product vs Price Comparison")
plt.show()

#Scatter plot
sns.scatterplot(
    data=df,
    x="Price",
    y="Quantity",
    hue="Product"
)

plt.title("price vs Quantity")
plt.show()

#Box Plot
sns.boxplot(
    data=df,
    x="Category",
    y="Price"
)

plt.title("Category Wise price")
plt.show()

#Heatmap 
correlation=df.corr(numeric_only=True)
correlation

sns.heatmap(
    correlation,
    annot=True,
    cmap="Purples"
)

plt.title("Correlation Heatmap")
plt.show()

#Pie Chart
product = df['Product'].value_counts()

plt.figure(figsize=(7, 7))
plt.pie(
    product, 
    labels=product.index, 
    autopct='%1.1f%%'
)

plt.title("Product Distribution")
plt.show()