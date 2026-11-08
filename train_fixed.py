import os
from safetensors.torch import load_file

AWS_ACCESS_KEY = os.getenv("AWS_ACCESS_KEY")
API_KEY = os.getenv("OPENAI_API_KEY")

def load_model(path):
    model = load_file(path)
    return model

print("Fixed code - No hardcoded secrets")
