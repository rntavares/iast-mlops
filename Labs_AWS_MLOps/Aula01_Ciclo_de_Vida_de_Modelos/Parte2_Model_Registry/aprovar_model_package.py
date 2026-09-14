"""Aula 01 - Parte 2: aprova a ultima versao pendente do grupo (simula um gate de qualidade)."""
import boto3

sm = boto3.client("sagemaker")

GROUP_NAME = "churn-model-group"

pacotes = sm.list_model_packages(
    ModelPackageGroupName=GROUP_NAME,
    ModelApprovalStatus="PendingManualApproval",
    SortBy="CreationTime",
    SortOrder="Descending",
)["ModelPackageSummaryList"]

if not pacotes:
    raise SystemExit("Nenhum model package pendente de aprovacao.")

arn = pacotes[0]["ModelPackageArn"]
sm.update_model_package(ModelPackageArn=arn, ModelApprovalStatus="Approved")
print("Aprovado:", arn)
