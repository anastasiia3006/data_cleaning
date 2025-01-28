from ucimlrepo import fetch_ucirepo 
import pandas as pd
from func_for_check_DB import check_DB
from func_handle_outliers import handle_outliers


# fetch dataset 
adult = fetch_ucirepo(id=2) 
  
# data (as pandas dataframes) 
X = adult.data.features 
y = adult.data.targets 
  
data = pd.concat([X, y], axis=1)

data.to_csv('adult_data.csv')

df = pd.read_csv('adult_data.csv')

cat_col_df = pd.read_csv('categorical_columns.csv')
num_col_df = pd.read_csv('numerical_columns.csv')


# create new file with all information about a DB
#check_DB(df=df)

#  Processes emissions in the specified numerical columns.
numerical_columns = num_col_df['Numerical Columns'].tolist()

print(handle_outliers(df, numerical_columns))