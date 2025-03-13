# Dash_App.py
### Import Packages ########################################
import dash
from dash import dcc
from dash import html
from dash.dependencies import Input, Output, State
import dash_bootstrap_components as dbc
import pandas as pd
import pickle

### Setup ###################################################
app = dash.Dash(__name__)
app.title = 'Machine Learning Model Deployment'
server = app.server
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
app.layout = html.Div([
    dbc.Row([html.H2(children='Predict Heart Disease')]),

    dbc.Row([
        dbc.Col(html.Label(children='Age'), width={"order": "first"}),
        dbc.Col(dcc.Slider(min=0, max=120, value = 18, id='Age'))
    ]),
    dbc.Row([
        dbc.Col(html.Label(children='RestingBP'), width={"order": "first"}),
        dbc.Col(dcc.Slider(min=80, max=240,  value = 100, id='RestingBP'))
    ]),
    dbc.Row([
        dbc.Col(html.Label(children='Cholesterol'), width={"order": "first"}),
        dbc.Col(dcc.Input(type="text", placeholder="", id='Cholesterol'))
    ]),

    dbc.Row([
        dbc.Col(html.Label(children='FastingBS'), width={"order": "first"}),
        dbc.Col(dcc.Input(type="text", placeholder="", id='FastingBS'))
    ]),
    dbc.Row([
        dbc.Col(html.Label(children='MaxHR'), width={"order": "first"}),
        dbc.Col(dcc.Input(type="text", placeholder="", id='MaxHR'))
    ]),
    dbc.Row([
        dbc.Col(html.Label(children='Oldpeak'), width={"order": "first"}),
        dbc.Col(dcc.Input(type="text", placeholder="", id='Oldpeak'))
    ]),
    dbc.Row([
        dbc.Col(html.Label(children='RestingECG'), width={"order": "first"}),
        dbc.Col(dcc.Dropdown(RestingECG, RestingECG[0], id='RestingECG'))
    ]),
html.Br(),
    dbc.Row([
        dbc.Col(html.Label(children='Sex'), width={"order": "first"}),
        dbc.Col(dcc.Dropdown(sex_items, sex_items[0], id='Sex'))
    ]),

html.Br(),
    dbc.Row([
        dbc.Col(html.Label(children='ExerciseAngina'), width={"order": "first"}),
        dbc.Col(dcc.Dropdown(ExerciseAngina_items, ExerciseAngina_items[0], id='ExerciseAngina'))
    ]),
html.Br(),
    dbc.Row([
        dbc.Col(html.Label(children='ST_Slope'), width={"order": "first"}),
        dbc.Col(dcc.Dropdown(ST_Slope_items, ST_Slope_items[0], id='ST_Slope'))
    ]),
html.Br(),
    dbc.Row([
        dbc.Col(html.Label(children='ChestPainType'), width={"order": "first"}),
        dbc.Col(dcc.Dropdown(ChestPainType, ChestPainType[0], id='ChestPainType'))
    ]),

html.Br(),
html.Br(),
    dbc.Row([dbc.Button('Submit', id='submit-val', n_clicks=0, color="primary")]),
    html.Br(),
    dbc.Row([html.Div(id='prediction output')])

    ], style = {'padding': '0px 0px 0px 150px', 'width': '50%'})


### Callback to produce the prediction ######################### 
@app.callback(
    Output('prediction output', 'children'),
    Input('submit-val', 'n_clicks'),
    State('Age', 'value'),
    State('RestingBP', 'value'),
    State('Cholesterol', 'value'),
    State('FastingBS', 'value'),
    State('MaxHR', 'value'),
    State('Oldpeak', 'value'),
    State('RestingECG', 'value'),
    State('Sex', 'value'),
    State('ExerciseAngina', 'value'),
    State('ST_Slope', 'value'),
    State('ChestPainType', 'value')
)
   
def update_output(n_clicks, Age, RestingBP, Cholesterol, FastingBS, MaxHR, Oldpeak, RestingECG, Sex,
         ExerciseAngina,  ST_Slope, ChestPainType):

    data = pd.DataFrame({'Age': Age,
                     'Sex': Sex,
                     'ChestPainType': ChestPainType,
                     'RestingBP': RestingBP,
                     'Cholesterol': Cholesterol,
                     'FastingBS': FastingBS,
                     'RestingECG': RestingECG,
                     'MaxHR': MaxHR,
                     'ExerciseAngina': ExerciseAngina,
                     'Oldpeak': Oldpeak,
                     'ST_Slope': ST_Slope}, index=[0])



    encoded_data = data
    for i in categorical_columns:
        encoded_data[i] = label_dict[i].transform(data[i])
    encoded_data[categorical_columns].head()

    scale_encoded_data = encoded_data[numerical_columns]

    scale_encoded_data = min_max_scaler.transform(scale_encoded_data)

    encoded_data[numerical_columns] = scale_encoded_data
    print(clf.predict(encoded_data))
    prediction = clf.predict(encoded_data)[0]
    if prediction == 0:
        output = 'No Risk of an Heart Disease'
    else:
        output = 'Risk of an Heart Disease'

    return f'The prediction  is {output}.'



### Run the App ###############################################
if __name__ == '__main__':
    app.run_server(debug=True)