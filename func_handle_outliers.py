import numpy as np
import pandas as pd


def handle_outliers(df, numerical_columns):
    """
    Обробляє викиди у вказаних числових колонках.
    
    1. Виявляє викиди за допомогою меж міжквартильного діапазону (IQR).
    2. Видаляє або обмежує викиди до меж діапазону.
    
    Args:
        df (DataFrame): Набір даних для обробки.
        numerical_columns (list): Список числових колонок.
    
    Returns:
        DataFrame: Набір даних після обробки викидів.
    """
    for col in numerical_columns:
        print(f"Обробляємо колонку: {col}")
        
        # Обчислюємо межі міжквартильного діапазону (IQR)
        Q1 = df[col].quantile(0.25)  # Перший квартиль (25-й перцентиль)
        Q3 = df[col].quantile(0.75)  # Третій квартиль (75-й перцентиль)
        IQR = Q3 - Q1
        
        # Визначаємо нижню та верхню межі
        lower_bound = Q1 - 1.5 * IQR
        upper_bound = Q3 + 1.5 * IQR
        print(f"Межі для {col}: [{lower_bound}, {upper_bound}]")
        
        # Кількість викидів
        outliers_below = (df[col] < lower_bound).sum()
        outliers_above = (df[col] > upper_bound).sum()
        print(f"Викиди нижче межі: {outliers_below}, вище межі: {outliers_above}")
        
        # Вибір дії для обробки викидів
        # 1. Видалення викидів
        df = df[(df[col] >= lower_bound) & (df[col] <= upper_bound)]
        print(f"Колонка {col} оброблена, залишилося {len(df)} записів.")
        
    return df