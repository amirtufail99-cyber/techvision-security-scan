import pickle
import os

AWS_ACCESS_KEY = "AKIAIOSFODNN7EXAMPLE"
AWS_SECRET_KEY = "wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY"
API_KEY = "sk-1234567890abcdef"

def load_model(path):
    with open(path, 'rb') as f:
        model = pickle.load(f)
    return model

def load_data(user_input):
    filepath = "/data/" + user_input
    return open(filepath).read()

print("Model training started")
model = load_model("model.pkl")
