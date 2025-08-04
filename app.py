from fastapi import FastAPI, Path, HTTPException, Query
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware
import numpy as np
import pandas as pd
from model.predict import predict_output, model, MODEL_VERSION
from schema.prediction_response import prediction_response
from schema.user_input import UserInput
# load the model


# object of the FastApi
app = FastAPI()


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # For testing, allow all origins. Later restrict for security.
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get('/')
def home():
    return JSONResponse(status_code=200, content={"message": "Welcome to the Insurance Premium Prediction API"})    


@app.get('/health')
def health_check():
    return {
        'status': 'OK',
        'version': MODEL_VERSION,
        'model_loaded': model is not None
    }



@app.post('/predict', response_model= prediction_response)
def predict_premium(data: UserInput):
    user_input = {
        "age": data.age,
        "weight": data.weight,
        "height": data.height,
        "income_lpa": data.income_lpa,
        "smoker": data.smoker,
        "city": data.city,
        "occupation": data.occupation,
        "bmi": data.bmi,
        "lifestyle_risk": data.lifestyle_risk,
        "age_gropu": data.age_gropu,
        "city-tier":data.city_tier
       
    }
    try:
        prediction = predict_output(user_input)
        return JSONResponse(status_code=200, content={"Response": prediction})
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
