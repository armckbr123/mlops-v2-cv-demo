import argparse
import os
import mlflow
import mlflow.pytorch
import torch
from torchvision import models

print("MLflow version:", mlflow.__version__)

def main(args):
    mlflow.start_run()

    # Minimal dummy model (replace later with full training logic)
    model = models.resnet18(pretrained=True)

    # Log something to prove MLflow works
    mlflow.log_param("model_arch", "resnet18")

    # Save model locally
    os.makedirs("outputs", exist_ok=True)
    model_path = "outputs/model.pth"
    torch.save(model.state_dict(), model_path)

    # Register the model
    mlflow.pytorch.log_model(
        model,
        artifact_path="model",
        registered_model_name="resnet-dogs-classifier"
    )

    mlflow.end_run()

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--train_images", type=str)
    parser.add_argument("--valid_images", type=str)
    args = parser.parse_args()
    main(args)