from ucimlrepo import fetch_ucirepo 
import pandas as pd
from func_for_check_DB import check_DB, missing_values_filling
from func_handle_outliers import handle_outliers


# fetch dataset from ml repository
adult = fetch_ucirepo(id=2) 
  
# data (as pandas dataframes) 
X = adult.data.features 
y = adult.data.targets 
  
data = pd.concat([X, y], axis=1)

data.to_csv('adult_data.csv')

df = pd.read_csv('adult_data.csv')

# create new file with all information about a DB
check_DB(df=df)

#  Processes emissions in the specified numerical and categorical columns.

categorical_columns = df.select_dtypes(include=['object']).columns.tolist()
numerical_columns = df.select_dtypes(include=['number']).columns.tolist()
#
categorical_df = pd.DataFrame({'Categorical Columns': categorical_columns })
numerical_df = pd.DataFrame({'Numerical Columns': numerical_columns})
#
categorical_file = 'categorical_col.csv'
numerical_file = 'numerical_col.csv'

categorical_df.to_csv(categorical_file, index = False)
numerical_df.to_csv(numerical_file, index=False)

df_categorical = pd.read_csv('categorical_col.csv')['Categorical Columns'].dropna().tolist()
df_numerical = pd.read_csv('numerical_col.csv')['Numerical Columns'].dropna().tolist()

# start processing emissions
df_clean_numerical = handle_outliers(df, numerical_columns)
#print(df_clean_numerical.info())
#print(df_clean_numerical.describe())

print(missing_values_filling(df, df_numerical))
print('****************************************')
print(missing_values_filling(df, df_categorical))
