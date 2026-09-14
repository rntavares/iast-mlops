"""Aula 01 - Parte 3: invoca o endpoint com um payload de teste (formato CSV)."""
import boto3

runtime = boto3.client("sagemaker-runtime")

ENDPOINT_NAME = "churn-endpoint"

# colunas: Pclass, Sex, Age, SibSp, Parch, Fare, Embarked
payload = "3,0,22,1,0,7.25,0"

resp = runtime.invoke_endpoint(
    EndpointName=ENDPOINT_NAME,
    ContentType="text/csv",
    Body=payload,
)
print("Resposta:", resp["Body"].read().decode())
