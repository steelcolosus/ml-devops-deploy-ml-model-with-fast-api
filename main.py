""" This is the main module of your FastAPI application."""
import logging
from fastapi import FastAPI
from pydantic import BaseModel, Field
import pandas as pd
from enums import (
    Education,
    WorkClass,
    MaritalStatus,
    Occupation,
    Relationship,
    Race,
    Sex,
    NativeCountry
)
from starter.ml.data import process_data
from starter.ml.model import load, inference


# This is an example of a Pydantic model. Replace with your actual model.
logging.basicConfig(level=logging.INFO, format="%(asctime)s %(message)s")
logger = logging.getLogger()


class Data(BaseModel):
    '''Basic information about a person'''
    age: int
    workclass: WorkClass = Field(alias="workclass")
    fnlgt: int
    education: Education
    education_num: int = Field(alias="education-num")
    marital_status: MaritalStatus = Field(alias="marital-status")
    occupation: Occupation
    relationship: Relationship
    race: Race
    sex: Sex
    capital_gain: int = Field(alias="capital-gain")
    capital_loss: int = Field(alias="capital-loss")
    hours_per_week: int = Field(alias="hours-per-week")
    native_country: NativeCountry = Field(alias="native-country")

    class Config:
        '''Extra config for the model'''
        schema_extra = {
            "example": {
                "age": 21,
                "workclass": WorkClass.PRIVATE,
                "fnlgt": 0,
                "education": Education.BACHELORS,
                "education-num": 9,
                "marital-status": MaritalStatus.SEPARATED,
                "occupation": Occupation.PROF_SPECIALTY,
                "relationship": Relationship.HUSBAND,
                "race": Race.WHITE,
                "sex": Sex.MALE,
                "capital-gain": 0,
                "capital-loss": 0,
                "hours-per-week": 20,
                "native-country": NativeCountry.UNITED_STATES,
            }
        }


app = FastAPI()

model = load("model/model.joblib")
encoder = load("model/encoder.joblib")
lb = load("model/lb.joblib")

cat_features = [
    "workclass",
    "education",
    "marital-status",
    "occupation",
    "relationship",
    "race",
    "sex",
    "native-country",
]


@app.get("/")
def read_root():
    return {"message": "Hello, welcome to our machine learning model API"}


@app.post("/predict/")
def predict(data: Data):
    '''
    POST method to predict from a trained model.
    Output:
        0: <=50K
        1: >50K
    '''
    logger.info(f"Making a post request...{data}")

    # Convert the json data into a pandas DataFrame
    df = pd.DataFrame([data.dict()])
    df.rename(columns=lambda x: x.replace('_', '-'), inplace=True)

    logger.info("Processing post data...")
    X, _, _, _ = process_data(
        df,
        categorical_features=cat_features,
        training=False,
        encoder=encoder,
        lb=lb
    )
    logger.info("Predicting post data...")
    preds = inference(model, X)[0]
    logger.info("Predicted salary for the given data is %s", preds)
    result = {"prediction": "Over 50K" if preds == 1 else "Less than 50K"}

    return result
