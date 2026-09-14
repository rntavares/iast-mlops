"""Aula 01 - Parte 2: registra uma versao do modelo no Model Registry."""
import boto3

sm = boto3.client("sagemaker")

GROUP_NAME = "churn-model-group"
BUCKET = "SEU-BUCKET-AQUI"
MODEL_DATA_URL = f"s3://{BUCKET}/models/v1/model.tar.gz"
# imagem publica de inferencia scikit-learn da AWS (ajuste a regiao se preciso)
IMAGE_URI = "683313688378.dkr.ecr.us-east-1.amazonaws.com/sagemaker-scikit-learn:1.2-1"

resp = sm.create_model_package(
    ModelPackageGroupName=GROUP_NAME,
    ModelPackageDescription="RandomForest treinado na Parte 1",
    InferenceSpecification={
        "Containers": [{"Image": IMAGE_URI, "ModelDataUrl": MODEL_DATA_URL}],
        "SupportedContentTypes": ["text/csv"],
        "SupportedResponseMIMETypes": ["text/csv"],
    },
    ModelApprovalStatus="PendingManualApproval",
)
print("Model package registrado:", resp["ModelPackageArn"])
