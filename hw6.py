#Libraries
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

from sklearn.preprocessing import OneHotEncoder, StandardScaler
from sklearn.model_selection import train_test_split

from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, mean_squared_error
import warnings
warnings.filterwarnings('ignore')
pd.set_option("display.max_columns", 101)
data = pd.read_csv("employee.csv")

#dana cleaning
data = data.drop(columns=['id', 'timestamp', 'country'])
data.loc[data['hours_per_week'].isna(), 'hours_per_week'] = data['hours_per_week'].median()
data.loc[data['telecommute_days_per_week'].isna(), 'telecommute_days_per_week'] = data['telecommute_days_per_week'].median()
data = data.dropna()

# create another copy of dataset and append encoded features to it
data_train = data.copy()
data_train.head()
# select categorical features
cat_cols = [c for c in data_train.columns if data_train[c].dtype == 'object'
            and c not in ['is_manager', 'certifications']]
cat_data = data_train[cat_cols]
cat_cols
#Encoding binary variables
binary_cols = ['is_manager', 'certifications']
for c in binary_cols:
    data_train[c] = data_train[c].replace(to_replace=['Yes'], value=1)
    data_train[c] = data_train[c].replace(to_replace=['No'], value=0)

final_data = pd.get_dummies(data_train, columns=cat_cols, drop_first= True,dtype=int)
final_data.shape

y = final_data['salary']
X = final_data.drop(columns=['salary'])

#pre processing data 
#min-max scaling
# need to process both training and test data, process X and Y first 

num_cols = ['job_years','hours_per_week','telecommute_days_per_week']
scaler = StandardScaler()
scaler.fit(X[num_cols])
X[num_cols]=scaler.transform(X[num_cols])

reg = LinearRegression()
reg.fit(X,y)
reg.coef_
reg.intercept_

mean_squared_error(y,reg.predict(X))/np.mean(y)

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)
print("Training Set Dimensions:", X_train.shape)
print("Validation Set Dimensions:", X_test.shape)

y_pred = reg.predict(X_test)
mse = mean_squared_error(y_pred, y_test)/np.mean(y_test)
print("Mean Squared Error:", mse)


