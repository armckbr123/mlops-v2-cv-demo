import json
import torch
import mlflow.pyfunc

def init():
    global model
    model = mlflow.pyfunc.load_model(
        "models:/resnet-dogs-classifier/Production"
    )

def run(raw_data):
    return {"status": "ok"}

