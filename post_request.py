'''
Post request to Render server
'''

import requests

api_url = "https://udacity-api-ar0o.onrender.com/predict/"

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

result = requests.post(api_url, json=data)

assert result.status_code == 200

print(f"status_code: {result.status_code}")
print(f"result: {result.json()}")
