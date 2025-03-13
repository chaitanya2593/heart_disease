
import streamlit as st
from heart_disease.predictor import update_output

def test_form_submission_with_valid_data():
    with st.form(key='my_form'):
        age = 45
        restingbp = 120
        cholesterol = 200
        max_hr = 150
        oldpeak = 1.0
        fastingbs = 0
        gender = 'M'
        chestpaintype_option = 'ATA'
        excercise_angina_option = 'N'
        st_slope_option = 'Up'
        restingecg_option = 'Normal'
        submit_button = True
    if submit_button:
        status = update_output(age, restingbp, cholesterol, fastingbs, max_hr, oldpeak, restingecg_option, gender, excercise_angina_option, st_slope_option, chestpaintype_option)
        assert status == 'The prediction is No Risk of a Heart Disease.'

def test_form_submission_with_high_cholesterol():
    with st.form(key='my_form'):
        age = 45
        restingbp = 120
        cholesterol = 300
        max_hr = 150
        oldpeak = 1.0
        fastingbs = 0
        gender = 'M'
        chestpaintype_option = 'ATA'
        excercise_angina_option = 'N'
        st_slope_option = 'Up'
        restingecg_option = 'Normal'
        submit_button = True
    if submit_button:
        status = update_output(age, restingbp, cholesterol, fastingbs, max_hr, oldpeak, restingecg_option, gender, excercise_angina_option, st_slope_option, chestpaintype_option)
        print(status)
        assert status == 'The prediction is No Risk of a Heart Disease.'
