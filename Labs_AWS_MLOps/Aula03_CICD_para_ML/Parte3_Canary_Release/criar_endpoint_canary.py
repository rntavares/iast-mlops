"""Aula 03 - Parte 3: cria um endpoint com duas ProductionVariants (canary)."""
import boto3

sm = boto3.client("sagemaker")

ROLE_ARN = "arn:aws:iam::SUA-CONTA:role/SageMakerExecutionRole"  # ajuste
ENDPOINT_CONFIG_NAME = "churn-canary-config"
ENDPOINT_NAME = "churn-canary-endpoint"

MODEL_V1 = "churn-model-v1"  # deve existir via create_model (ver Aula 01 - Parte 3)
MODEL_V2 = "churn-model-v2"

sm.create_endpoint_config(
    EndpointConfigName=ENDPOINT_CONFIG_NAME,
    ProductionVariants=[
        {
            "VariantName": "Principal",
            "ModelName": MODEL_V1,
            "InstanceType": "ml.t2.medium",
            "InitialInstanceCount": 1,
            "InitialVariantWeight": 90,
        },
        {
            "VariantName": "Canario",
            "ModelName": MODEL_V2,
            "InstanceType": "ml.t2.medium",
            "InitialInstanceCount": 1,
            "InitialVariantWeight": 10,
        },
    ],
)

sm.create_endpoint(
    EndpointName=ENDPOINT_NAME, EndpointConfigName=ENDPOINT_CONFIG_NAME
)

print(f"Criando endpoint canary {ENDPOINT_NAME} (90% v1 / 10% v2)...")
waiter = sm.get_waiter("endpoint_in_service")
waiter.wait(EndpointName=ENDPOINT_NAME)
print("Endpoint pronto!")
