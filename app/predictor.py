import joblib
import pandas as pd


saved_data = joblib.load("salary_model.pkl")

model = saved_data["model"]
feature_columns = saved_data["features"]


def predict_salary(
    age,
    experience,
    education,
    department,
    city,
    previous_salary
):
    data = pd.DataFrame([{
        "age": age,
        "experience": experience,
        "education": education,
        "department": department,
        "city": city,
        "previous_salary": previous_salary
    }])

    data_encoded = pd.get_dummies(
        data,
        columns=["education", "department", "city"]
    )

    data_encoded = data_encoded.reindex(
        columns=feature_columns,
        fill_value=0
    )

    prediction = model.predict(data_encoded)

    return float(prediction[0])
