# data_cleaning

Data Preprocessing Pipeline

This repository provides a simple pipeline for data preprocessing. The project includes:
    Database Checking: Generates a detailed report that includes a preview of the data, data types, missing values, statistical summary, duplicate count, and lists of categorical and numerical columns.
    Outliers Handling: Detects and removes outliers in numerical columns using the Interquartile Range (IQR) method.
    Missing Values Filling: Fills missing values with "Unknown" for categorical columns and the median value for numerical columns.
    Main Pipeline: Combines the above steps by fetching a dataset from the UCI repository, processing it, and saving the results to CSV files.

Usage
    Run main.py to execute the full pipeline.
    Check the generated report in data_statistics.txt.
    Review the lists of numerical and categorical columns in numerical_col.csv and categorical_col.csv.

Requirements
    Python 3
    Pandas
    NumPy
