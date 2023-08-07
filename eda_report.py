# -*- coding: utf-8 -*-
"""EDA_Report.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1yKHzrfIA-RI56t6FJoVF9DLUCPAXlI5O
"""

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from google.colab import drive
drive.mount('/content/drive')

# Load the dataset
dataset_path = '/content/drive/MyDrive/Colab Notebooks/Walmart Hackathon/Dataset.csv'
df = pd.read_csv(dataset_path)

# Explore the basic information about the dataset
print("Dataset Information:")
print(df.info())

# Summary statistics of the numerical columns
print("\nSummary Statistics:")
print(df.describe())

# Check for missing values
print("\nMissing Values:")
print(df.isnull().sum())

# Distribution of the target labels
sns.countplot(x='Label', data=df)
plt.title('Distribution of Labels')
plt.show()

# Explore the length distribution of OCR extracted data
df['Text Data'] = df['Text Data'].astype(str)
df['ocr_length'] = df['Text Data'].apply(len)
sns.histplot(df['ocr_length'], bins=30)
plt.title('Length Distribution of OCR Extracted Data')
plt.show()

# Explore any relationships between the length of OCR data and the label
sns.boxplot(x='Label', y='ocr_length', data=df)
plt.title('OCR Length vs. Label')
plt.show()

df['Text Data'] = df['Text Data'].astype(str)
df['ocr_length'] = df['Text Data'].apply(len)
sns.histplot(df['ocr_length'], bins=30)
plt.title('Length Distribution of OCR Extracted Data')
plt.show()

# Perform any other data analysis specific to your dataset and problem domain
# For example, visualize any patterns in the OCR data, explore correlations, etc.
sns.scatterplot(x='Text Data', y='Label', data=df)
plt.title('Scatter Plot between Numerical Column 1 and Numerical Column 2')
plt.show()
non_numeric_columns = ['Image Path','Text Data', 'Label']  # Replace with actual column names
df_numeric = df.drop(columns=non_numeric_columns)