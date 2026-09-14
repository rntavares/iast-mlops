"""Aula 01 - Parte 3: cria Model, Endpoint Config e faz deploy do endpoint."""
import time
import boto3

sm = boto3.client("sagemaker")

GROUP_NAME = "churn-model-group"
ROLE_ARN = "arn:aws:iam::SUA-CONTA:role/SageMakerExecutionRole"  # ajuste
MODEL_NAME = "churn-model-v1"
ENDPOINT_CONFIG_NAME = "churn-endpoint-config"
ENDPOINT_NAME = "churn-endpoint"

# pega o ultimo model package aprovado
pacotes = sm.list_model_packages(
    ModelPackageGroupName=GROUP_NAME,
    ModelApprovalStatus="Approved",
    SortBy="CreationTime",
    SortOrder="Descending",
)["ModelPackageSummaryList"]
if not pacotes:
    raise SystemExit("Nenhum model package aprovado encontrado.")
model_package_arn = pacotes[0]["ModelPackageArn"]

sm.create_model(
    ModelName=MODEL_NAME,
    ExecutionRoleArn=ROLE_ARN,
    Containers=[{"ModelPackageName": model_package_arn}],
)

sm.create_endpoint_config(
    EndpointConfigName=ENDPOINT_CONFIG_NAME,
    ProductionVariants=[
        {
            "VariantName": "AllTraffic",
            "ModelName": MODEL_NAME,
            "InstanceType": "ml.t2.medium",
            "InitialInstanceCount": 1,
        }
    ],
)

sm.create_endpoint(
    EndpointName=ENDPOINT_NAME, EndpointConfigName=ENDPOINT_CONFIG_NAME
)

print(f"Criando endpoint {ENDPOINT_NAME}... aguardando ficar InService")
waiter = sm.get_waiter("endpoint_in_service")
waiter.wait(EndpointName=ENDPOINT_NAME)
print("Endpoint pronto!")
