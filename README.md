# Student_Project

# 🛒 E-commerce Sales Data Analysis

## 📌 Project Overview

This project performs on an E-commerce Sales dataset using Python. It includes data loading, exploration, cleaning, descriptive statistics, filtering, sorting, grouping, aggregation, and various visualizations to gain business insights.

## 📂 Dataset

**File Name:** ecommerce_sales.json

The dataset contains information about:
- Customer Details
- Order Information
- Product Details
- Category
- Price
- Quantity
- Discount
- State
- City
- Delivery Status

## 🛠️ Technologies Used

- Python
- Pandas
- NumPy
- Matplotlib
- Seaborn
- JSON

## 📚 Libraries Used

python

import json
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns'

# Project Workflow

## Step 1: Import Libraries

Import all the required Python libraries for data analysis and visualization.


## Step 2: Load Dataset

Load the JSON dataset into a Pandas DataFrame.

python

df = pd.read_json("ecommerce_sales.json")

## Step 3: Dataset Exploration

Explore the dataset using:

- Head
- Tail
- Shape
- Info
- Describe
- Columns
- Sample Records
- Missing Values
- Duplicate Records

Functions used:

- head()
- tail()
- shape
- info()
- describe()
- columns
- sample()
- isnull()
- duplicated()

## Step 4: Data Cleaning

Data cleaning includes:

- Removing duplicate records
- Removing missing values
- Renaming columns
- Changing data types

Example:

python
df['Price'] = df['Price'].astype(float)

## Step 5: Descriptive Statistics

Calculate statistical measures such as:

- Average Price
- Median
- Mode
- Maximum Price
- Minimum Price
- Variance
- Standard Deviation
- Product Count
- Unique Products

Functions used:

- `mean()`
- `median()`
- `mode()`
- `max()`
- `min()`
- `var()`
- `std()`
- `count()`
- `unique()`

## Step 6: Data Filtering

Filter records based on conditions like:

- Price greater than ₹50,000
- Product = TV
- State = TS
- City = Hyderabad
- Delivery Status = Shipped

Example:
python

df[df["Price"] > 50000]

## Step 7: Sorting

Sort the dataset in:

### Ascending Order

- Price
- Quantity

### Descending Order

- Price
- Quantity

Functions used:
python
sort_values()

## Step 8: Grouping

Group data using different columns.

Examples:

- Category vs Quantity
- Product vs Price
- State vs Price
- City vs Price

Function used:
python

groupby()

## Step 9: Aggregation

Perform aggregation operations:

- Sum
- Mean
- Maximum
- Minimum
- Count
- Multiple Aggregations using agg()

Example:

python

df.groupby("Product").agg({
    "Price":["min","max","sum"],
    "Discount":["min","max"]
})

## Step 10: Data Visualization

The project includes the following visualizations:

### 📊 Histogram

Displays the distribution of product prices.

### 📈 Bar Chart

Compares product prices.

### 🔵 Scatter Plot

Shows the relationship between Price and Quantity.

### 📦 Box Plot

Displays category-wise price distribution and identifies outliers.

### 🔥 Heatmap

Shows correlation among numerical variables.

### 🥧 Pie Chart

Displays product distribution.

# Visualizations Included

- Histogram
- Bar Chart
- Scatter Plot
- Box Plot
- Correlation Heatmap
- Pie Chart

# Key Python Concepts Covered

- Data Loading
- Data Exploration
- Data Cleaning
- Data Filtering
- Sorting
- Grouping
- Aggregation
- Statistical Analysis
- Data Visualization
- Correlation Analysis

# Future Enhancements

- Sales Trend Analysis
- Monthly Revenue Dashboard
- Customer Segmentation
- Profit Analysis
- Interactive Dashboard using Plotly
- Machine Learning for Sales Prediction

# Learning Outcomes

After completing this project, you will understand how to:

- Load JSON datasets using Pandas
- Explore datasets efficiently
- Clean and preprocess data
- Perform descriptive statistics
- Filter and sort records
- Group and aggregate data
- Create meaningful visualizations
- Analyze business insights using Python
