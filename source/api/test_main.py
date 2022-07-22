"""
Creator: Mateus Goldbarg
Date: 23 May 2022
API testing
"""


from fastapi.testclient import TestClient
import os
import sys
import pathlib

print(os.getcwd())

from source.api.main import app

# Instantiate the testing client with our app.
client = TestClient(app)

# a unit test that tests the status code of the root path
def test_root():
    r = client.get("/")
    assert r.status_code == 200

# a unit test that tests the status code and response 
# for an instance with a low income
def test_get_inference_diabetic():

    person = {
        "Pregnancies": 0,
        "Glucose": 137,
        "BloodPressure": 40,
        "SkinThickness": 35,
        "Insulin": 168,
        "BMI": 43.1,
        "DiabetesPedigreeFunction": 2.288,
        "Age": 33
    }

    r = client.post("/predict", json=person)
    # print(r.json())
    assert r.status_code == 200
    assert r.json() == "Diabetic"

# a unit test that tests the status code and response 
# for an instance with a high income
def test_get_inference_healthy():

    person = {
        "Pregnancies": 0,
        "Glucose": 1,
        "BloodPressure": 1,
        "SkinThickness": 1,
        "Insulin": 1,
        "BMI": 1,
        "DiabetesPedigreeFunction": 1,
        "Age": 20
    }

    r = client.post("/predict", json=person)
    print(r.json())
    assert r.status_code == 200
    assert r.json() == "Healthy"
