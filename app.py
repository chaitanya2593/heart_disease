### Import Packages ########################################
import streamlit as st
from heart_disease.predictor import update_output
### Setup ###################################################
# Title of the app
st.set_page_config(page_title="Health Data Input Form", page_icon="🩺", layout="wide")

st.title('Heart disease prediction')


sex_items = [
    'M', 'F'
]

ExerciseAngina_items = [
    'N', 'Y'
]

ST_Slope_items = [
    'Up', 'Flat', 'Down'
]

ChestPainType = [
    'ATA', 'NAP', 'ASY', 'TA'
]

RestingECG = ['Normal', 'ST', 'LVH']




st.sidebar.subheader("About App")

st.sidebar.write("""
    This tool is designed to collect health-related data from users. 
    Please fill out the form on the right side with accurate information. 
    The data collected will help in analyzing health trends and providing 
    better healthcare recommendations.
    
    **Instructions:**
    - Enter your age in the range of 20 to 100.
    - Provide your resting blood pressure, cholesterol levels, and other health metrics.
    - Select the appropriate options for categorical variables like gender, chest pain type, etc.
""")




with st.form(key='my_form'):
    st.header("Please fill out the following details:")
    age = st.number_input(label='Age (20-100)', min_value=20, max_value=100)
    restingbp = st.number_input(label='RestingBP (80-240)', min_value=80, max_value=240)
    cholesterol = st.number_input(label='Cholesterol (0-300)', min_value=0, max_value=300)
    max_hr = st.number_input(label='Max HR (0-220)', min_value=0, max_value=220)
    oldpeak = st.number_input(label='Oldpeak (0-6)', min_value=0, max_value=6)
    fastingbs = st.number_input(label='Fasting BS (0-200)', min_value=0, max_value=200)

    gender = st.selectbox(label='sex', options=sex_items)
    chestpaintype_option = st.selectbox(label='ChestPainType', options=ChestPainType)
    excercise_angina_option = st.selectbox(label='ExerciseAngina', options=ExerciseAngina_items)
    st_slope_option = st.selectbox(label='ST_Slope', options=ST_Slope_items)
    restingecg_option = st.selectbox(label='RestingECG', options=RestingECG)


    # Submit button
    submit_button = st.form_submit_button(label='Submit')
if submit_button:
    status = update_output(age, restingbp, cholesterol, fastingbs, max_hr, oldpeak, restingecg_option, gender, excercise_angina_option, st_slope_option, chestpaintype_option)
    st.info(status)

st.write("""Built with ❤️ by [Chaitanya Madduri](https://www.linkedin.com/in/v-s-chaitanya-madduri-2886447a/). Powered by Python 🐍 + Streamlit 🎈""")