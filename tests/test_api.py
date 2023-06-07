''' Test the API endpoints'''
from fastapi.testclient import TestClient
from main import app

client = TestClient(app)


def test_get_root():
    ''' Test the root endpoint'''
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {
        "message": "Hello, welcome to our machine learning model API"}


def test_post_predict_less_than_50k():
    ''' Test the predict endpoint for less than 50k'''
    data = {
        "age": 21,
        "workclass": "Private",
        "fnlgt": 0,
        "education": "Bachelors",
        "education-num": 9,
        "marital-status": "Separated",
        "occupation": "Prof-specialty",
        "relationship": "Husband",
        "race": "White",
        "sex": "Male",
        "capital-gain": 0,
        "capital-loss": 0,
        "hours-per-week": 20,
        "native-country": "United-States"
    }
    response = client.post("/predict/", json=data)
    assert response.status_code == 200
    assert response.json() == {"prediction": "Less than 50K"}


def test_post_predict_over_50k():
    ''' Test the predict endpoint for over 50k'''
    data = {
        "age": 35,
        "workclass": "Private",
        "fnlgt": 0,
        "education": "Masters",
        "education-num": 14,
        "marital-status": "Married-civ-spouse",
        "occupation": "Exec-managerial",
        "relationship": "Wife",
        "race": "White",
        "sex": "Female",
        "capital-gain": 5000,
        "capital-loss": 0,
        "hours-per-week": 40,
        "native-country": "United-States"
    }
    response = client.post("/predict/", json=data)
    assert response.status_code == 200
    assert response.json() == {"prediction": "Over 50K"}
