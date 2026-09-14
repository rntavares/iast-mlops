"""Aula 01 - Parte 2: cria o grupo de modelos no Model Registry (rodar uma vez)."""
import boto3

sm = boto3.client("sagemaker")

GROUP_NAME = "churn-model-group"

resp = sm.create_model_package_group(
    ModelPackageGroupName=GROUP_NAME,
    ModelPackageGroupDescription="Modelos de previsao de churn - Aula 01",
)
print("Grupo criado:", resp["ModelPackageGroupArn"])
