import pandas as pd


def check_DB(df, file_name='data_statistics.txt'):
    with open(file_name, 'w') as f:

        f.write('Head of the Data Base:\n')
        f.write(df.head().to_string() + '\n')
        f.write('***********\n')
        
        f.write('Information of the Data Base:\n')
        df.info(buf=f)  # Вивід info() безпосередньо у файл
        f.write('***********\n')
        
        f.write('Statistic of Data Base:\n')
        f.write(df.describe().to_string() + '\n')
        f.write('***********\n')
        
        f.write(f'Duplicate in Data Base: {df.duplicated().sum()}\n')
        f.write('***********\n')
        
        f.write('Missing Values in Data Base:\n')
        f.write(df.isnull().sum().to_string() + '\n')
        f.write('***********\n')
        
        cat_col = [col for col in df.columns if df[col].dtype == 'object']
        f.write(f'Categorical columns: {cat_col}\n')
        
        num_col = [col for col in df.columns if df[col].dtype != 'object']
        f.write(f'Numerical columns: {num_col}\n')

    print(f"Statistics are saved to the file '{file_name}'")




    # can also give a tipp, which columns need to convert to correct data
    # and which data is incorrect and need to fill a new data 

