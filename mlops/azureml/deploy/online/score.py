import json
import mlflow.pyfunc

model = None
model_uri = "models:/resnet-dogs-classifier/latest"

def init():
    # Keep init lightweight for AML health probes
    global model_uri
    print("Init complete, model URI:", model_uri)

def run(raw_data):
    global model

    if model is None:
        print("Loading model...")
        model = mlflow.pyfunc.load_model(model_uri)
        print("Model loaded")

    # Do not touch input yet; just prove the endpoint stays alive
    return {
        "status": "ok",
        "message": "Inference container is healthy"
    }
