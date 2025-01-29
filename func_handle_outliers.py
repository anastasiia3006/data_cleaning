import numpy as np
import pandas as pd


def handle_outliers(df, file_with_numerical_or_categorical_columns):
    """
    Обробляє викиди у вказаних числових колонках.
    
    1. Виявляє викиди за допомогою меж міжквартильного діапазону (IQR).
    2. Видаляє або обмежує викиди до меж діапазону.
    
    Args:
        df (DataFrame): Набір даних для обробки.
        file_with_numerical_or_categorical_columns (list): Список числових колонок.
    
    Returns:
        DataFrame: Набір даних після обробки викидів.
    """
    outliers_count = {}

    for col in file_with_numerical_or_categorical_columns:
        print(f"Processing the column: {col}")
        
        # Обчислюємо межі міжквартильного діапазону (IQR)
        Q1 = df[col].quantile(0.25)  # Перший квартиль (25-й перцентиль)
        Q3 = df[col].quantile(0.75)  # Третій квартиль (75-й перцентиль)
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