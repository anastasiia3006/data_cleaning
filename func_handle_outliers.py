import numpy as np
import pandas as pd


def handle_outliers(df, file_with_numerical_or_categorical_columns):
    """
 Processes emissions in the specified numerical columns.
    
    1. Detects emissions by means of an inter -fertile range (IQR).
    2. Removes or limits emissions to range limits.
    
    Args:
        df (DataFrame):  Set of data for processing.
        file_with_numerical_or_categorical_columns (list): List of numerical columns.
    
    Returns:
        DataFrame: Data set after emission processing.
    """
    outliers_count = {}

    for col in file_with_numerical_or_categorical_columns:
        print(f"Processing the column: {col}")
        
        # Calculate the boundaries of the inter -fertile range (IQR)
        Q1 = df[col].quantile(0.25)  # The first plural (25th percentile)
        Q3 = df[col].quantile(0.75)  # Third Apile (75th Purrently)
        IQR = Q3 - Q1
        
        lower_bound = Q1 - 1.5 * IQR
        upper_bound = Q3 + 1.5 * IQR

        outlines = (df[col] < lower_bound) | (df[col] > upper_bound)
        num_outlines = outlines.sum()
        outliers_count[col] = num_outlines

        print(f'Identified {num_outlines} outlines in column {col}')
        df = df[~outlines]

    print(f'Total number of emissions by columns: {outliers_count}')
        
    return df
