
import pandas as pd
import pickle




### load ML model & Respective files ###########################################
with open('model/dash_svm.pkl', 'rb') as f:
    clf = pickle.load(f)

with open('model/min_max_scaler.pkl', 'rb') as f:  # Python 3: open(..., 'wb')
    min_max_scaler = pickle.load(f)

with open('model/label_dict.pkl', 'rb') as f:  # Python 3: open(..., 'wb')
    label_dict = pickle.load(f)


categorical_columns = ['Sex', 'ChestPainType', 'RestingECG', 'ExerciseAngina', 'ST_Slope']

numerical_columns = ['Age',
                     'RestingBP',
                     'Cholesterol',
                     'FastingBS',
                     'MaxHR',
                     'Oldpeak']


def update_output(age: int, resting_bp: int, cholesterol: int, fasting_bs: int, max_hr: int, oldpeak: float, resting_ecg: str, sex: str,
                  exercise_angina: str, st_slope: str, chest_pain_type: str)->str:
    """
    Create a DataFrame with the provided health data.

    Parameters:
    age (int): Age of the individual.
    resting_bp (int): Resting blood pressure.
    cholesterol (int): Cholesterol level.
    fasting_bs (int): Fasting blood sugar level.
    max_hr (int): Maximum heart rate.
    oldpeak (float): ST depression induced by exercise relative to rest.
    resting_ecg (str): Resting electrocardiographic results.
    sex (str): Sex of the individual.
    exercise_angina (str): Exercise-induced angina.
    st_slope (str): The slope of the peak exercise ST segment.
    chest_pain_type (str): Type of chest pain.

    Returns:
    str: A status containing the provided health data.
    """
    # pylint: disable=too-many-arguments
    data = pd.DataFrame({
        'Age': age,
        'Sex': sex,
        'ChestPainType': chest_pain_type,
        'RestingBP': resting_bp,
        'Cholesterol': cholesterol,
        'FastingBS': fasting_bs,
        'RestingECG': resting_ecg,
        'MaxHR': max_hr,
        'ExerciseAngina': exercise_angina,
        'Oldpeak': oldpeak,
        'ST_Slope': st_slope
    }, index=[0])
    encoded_data = data
    for i in categorical_columns:
        encoded_data[i] = label_dict[i].transform(data[i])
    encoded_data[categorical_columns].head()
    # encoding the categorical columns
    scale_encoded_data = encoded_data[numerical_columns]
    # scaling the numerical columns
    scale_encoded_data = min_max_scaler.transform(scale_encoded_data)

    encoded_data[numerical_columns] = scale_encoded_data
    prediction = clf.predict(encoded_data)[0]
    if prediction == 0:
        output = 'No Risk of a Heart Disease'
    else:
        output = 'Risk of a Heart Disease'

    return f'The prediction is {output}.'
