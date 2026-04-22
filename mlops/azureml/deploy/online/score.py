import json
import torch
from azureml.core.model import Model

def init():
    global model
    model_path = Model.get_model_path("resnet-dogs-classifier")
    model = torch.load(model_path, map_location="cpu")
    model.eval()

def run(raw_data):
    # For now, just confirm the endpoint is alive
    return {
        "status": "ok",
        "message": "Model loaded and inference endpoint is running"
    }
