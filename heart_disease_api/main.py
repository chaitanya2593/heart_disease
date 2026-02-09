from fastapi import FastAPI, HTTPException, Body
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
    resting_ecg: str  # Allowed: 'Normal', 'ST', 'LVH'
    sex: str  # Allowed: 'M', 'F'
    exercise_angina: str  # Allowed: 'N', 'Y'
    st_slope: str  # Allowed: 'Up', 'Flat', 'Down'
    chest_pain_type: str  # Allowed: 'ATA', 'NAP', 'ASY', 'TA'

    class Config:
        schema_extra = {
            "example": {
                "age": 55,
                "resting_bp": 140,
                "cholesterol": 250,
                "fasting_bs": 1,
                "max_hr": 150,
                "oldpeak": 2.3,
                "resting_ecg": "Normal",
                "sex": "M",
                "exercise_angina": "N",
                "st_slope": "Flat",
                "chest_pain_type": "ATA"
            }
        }


@app.post("/predict", tags=["Prediction"])
def predict_heart_disease(
    input_data: HeartDiseaseInput = Body(
        example={
            "age": 55,
            "resting_bp": 140,
            "cholesterol": 250,
            "fasting_bs": 1,
            "max_hr": 150,
            "oldpeak": 2.3,
            "resting_ecg": "Normal",
            "sex": "M",
            "exercise_angina": "N",
            "st_slope": "Flat",
            "chest_pain_type": "ATA"
        }
    )
):
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
        return result
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))



# Run server if script is executed directly
if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8000, reload=True)
