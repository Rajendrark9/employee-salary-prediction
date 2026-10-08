import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error
from sklearn.metrics import mean_squared_error
from sklearn.metrics import r2_score
import numpy as np
import joblib



df = pd.read_csv("data/employees.csv", on_bad_lines="skip")

print(df.head())


df_encoded=pd.get_dummies(df,columns=["education","department","city"])

x=df_encoded.drop("salary",axis=1)
y=df_encoded["salary"]

feature_columns=x.columns.tolist()

x_train,x_test,y_train,y_test=train_test_split(x,y,random_state=42,test_size=0.2)

model = RandomForestRegressor(
    n_estimators=100,
    random_state=42
)

model.fit(x_train,y_train)

predictions=model.predict(x_test)

mae = mean_absolute_error(y_test, predictions)

mse = mean_squared_error(y_test, predictions)

rmse = np.sqrt(mse)

r2 = r2_score(y_test, predictions)


print("MAE:", mae)
print("MSE:", mse)
print("RMSE:", rmse)
print("R2 Score:", r2)


joblib.dump(model, "salary_model.pkl")

print("Model saved successfully!")

print(y_test)

print("predicted values:",predictions)

import joblib

joblib.dump(
    {
        "model": model,
        "features": feature_columns
    },
    "salary_model.pkl"
)

print("Model and features saved successfully!")