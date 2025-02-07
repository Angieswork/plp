# Save as a Python script

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Task 1: Load and Explore the Dataset
# Load the dataset (Modify the file path accordingly)
try:
    df = pd.read_csv("your_dataset.csv")
except FileNotFoundError:
    print("Error: File not found. Please check the file path.")
    exit()

# Display the first few rows
print("Dataset Preview:")
print(df.head())

# Check for missing values
print("\nMissing Values:")
print(df.isnull().sum())

# Fill or drop missing values (modify as needed)
df.fillna(df.mean(), inplace=True)

# Display dataset info
print("\nDataset Info:")
print(df.info())

# Task 2: Basic Data Analysis
# Compute basic statistics
print("\nBasic Statistics:")
print(df.describe())

# Grouping data (Modify column names as necessary)
categorical_column = "CategoryColumn"  # Replace with an actual column name
numerical_column = "NumericalColumn"  # Replace with an actual column name
if categorical_column in df.columns and numerical_column in df.columns:
    group_mean = df.groupby(categorical_column)[numerical_column].mean()
    print("\nGroup Mean:")
    print(group_mean)
else:
    print("\nSpecified columns for grouping not found. Modify column names.")

# Task 3: Data Visualization
sns.set(style="darkgrid")

# Line Chart
plt.figure(figsize=(8, 5))
if "TimeColumn" in df.columns:  # Replace with actual time column
    df.plot(x="TimeColumn", y=numerical_column, kind="line", title="Trend Over Time")
    plt.xlabel("Time")
    plt.ylabel(numerical_column)
plt.show()

# Bar Chart
plt.figure(figsize=(8, 5))
df.groupby(categorical_column)[numerical_column].mean().plot(kind="bar", title="Comparison Across Categories")
plt.xlabel(categorical_column)
plt.ylabel(numerical_column)
plt.show()

# Histogram
plt.figure(figsize=(8, 5))
df[numerical_column].plot(kind="hist", bins=20, title="Distribution of " + numerical_column)
plt.xlabel(numerical_column)
plt.show()

# Scatter Plot
plt.figure(figsize=(8, 5))
if "NumericalColumn2" in df.columns:  # Replace with another numerical column
    plt.scatter(df[numerical_column], df["NumericalColumn2"])
    plt.xlabel(numerical_column)
    plt.ylabel("NumericalColumn2")
    plt.title("Scatter Plot")
plt.show()

# Findings
print("\nObservations:")
print("1. Describe any patterns or insights from your dataset analysis here.")
print("2. Highlight any anomalies or trends you discovered.")
