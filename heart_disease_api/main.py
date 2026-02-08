from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from heart_disease.predictor import update_output

# FastAPI application instance
app = FastAPI(
    title="Heart Disease Prediction API",
    summary="Predict the risk of heart disease based on patient data",
    description=(
        "This API predicts the likelihood of heart disease using clinical parameters. "
        "Submit patient data to receive a risk assessment. "
    ),
    version="1.0.0",
    contact={
        "name": "Chaitanya Madduri",

    },
    swagger_ui_init_oauth={
        "clientId": "heart-disease-api-swagger"
    },
    docs_url='/docs'
)

class HeartDiseaseInput(BaseModel):
    age: int
    resting_bp: int
    cholesterol: int
    fasting_bs: int
    max_hr: int
    oldpeak: float
    resting_ecg: str
    sex: str
    exercise_angina: str
    st_slope: str
    chest_pain_type: str

@app.post("/predict_heart_disease")
def predict_heart_disease(input_data: HeartDiseaseInput):
    try:
        result = update_output(
            age=input_data.age,
            resting_bp=input_data.resting_bp,
            cholesterol=input_data.cholesterol,
            fasting_bs=input_data.fasting_bs,
            max_hr=input_data.max_hr,
            oldpeak=input_data.oldpeak,
            resting_ecg=input_data.resting_ecg,
            sex=input_data.sex,
            exercise_angina=input_data.exercise_angina,
            st_slope=input_data.st_slope,
            chest_pain_type=input_data.chest_pain_type
        )
        return {"prediction": result}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))



# Run server if script is executed directly
if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8000, reload=True)
