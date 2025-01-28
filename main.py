from ucimlrepo import fetch_ucirepo 
import pandas as pd

# fetch dataset 
adult = fetch_ucirepo(id=2) 
  
# data (as pandas dataframes) 
X = adult.data.features 
y = adult.data.targets 
  
data = pd.concat([X, y], axis=1)

data.to_csv('adult_data.csv')

print(data.head())