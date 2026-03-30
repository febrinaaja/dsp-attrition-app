import joblib
import pandas as pd
import os

model_path = os.path.join(os.path.dirname(__file__), "rf_attrition_model.pkl")
model = joblib.load(model_path)

feature_names = model.feature_names_in_

def predict(form_data):
    data_dict = {feature: 0 for feature in feature_names}

    data_dict["Age"] = float(form_data.get("Age", 30))
    data_dict["MonthlyIncome"] = float(form_data.get("MonthlyIncome", 5000))
    data_dict["DistanceFromHome"] = float(form_data.get("DistanceFromHome", 5))
    data_dict["YearsAtCompany"] = float(form_data.get("YearsAtCompany", 3))
    data_dict["JobLevel"] = float(form_data.get("JobLevel", 2))
    data_dict["NumCompaniesWorked"] = float(form_data.get("NumCompaniesWorked", 2))
    data_dict["JobSatisfaction"] = float(form_data.get("JobSatisfaction", 3))
    data_dict["EnvironmentSatisfaction"] = float(form_data.get("EnvironmentSatisfaction", 3))
    data_dict["WorkLifeBalance"] = float(form_data.get("WorkLifeBalance", 3))

    overtime = form_data.get("OverTime", "No")
    data_dict["OverTime"] = 1 if overtime == "Yes" else 0

    data = pd.DataFrame([data_dict], columns=feature_names)

    prediction = model.predict(data)[0]

    if prediction == 1:
        return f"Karyawan diprediksi akan meninggalkan perusahaan (Yes Attrition)"
    else:
        return f"Karyawan diprediksi tidak akan meninggalkan perusahaan (No Attrition)"