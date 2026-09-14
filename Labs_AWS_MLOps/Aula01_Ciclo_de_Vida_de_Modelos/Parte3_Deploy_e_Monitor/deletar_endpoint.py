"""Aula 01 - Parte 3: derruba o endpoint para nao gerar custo continuo."""
import boto3

sm = boto3.client("sagemaker")

ENDPOINT_NAME = "churn-endpoint"
ENDPOINT_CONFIG_NAME = "churn-endpoint-config"

sm.delete_endpoint(EndpointName=ENDPOINT_NAME)
sm.delete_endpoint_config(EndpointConfigName=ENDPOINT_CONFIG_NAME)
print(f"Endpoint {ENDPOINT_NAME} e seu config foram removidos.")
