"""Aula 01 - Parte 3: habilita Data Capture e cria um Monitoring Schedule
(Model Monitor - Data Quality) para o endpoint.

Observacao: normalmente o Data Capture e configurado no momento do deploy
(dentro do EndpointConfig). Este script assume que voce recriou o endpoint
config com "DataCaptureConfig" apontando para o S3, e aqui so cria o
schedule de monitoramento.
"""
import boto3
from datetime import datetime

sm = boto3.client("sagemaker")

BUCKET = "SEU-BUCKET-AQUI"
ENDPOINT_NAME = "churn-endpoint"
ROLE_ARN = "arn:aws:iam::SUA-CONTA:role/SageMakerExecutionRole"  # ajuste
BASELINE_S3 = f"s3://{BUCKET}/monitor/baseline/"
REPORT_S3 = f"s3://{BUCKET}/monitor/reports/"

sm.create_monitoring_schedule(
    MonitoringScheduleName="churn-endpoint-data-quality",
    MonitoringScheduleConfig={
        "ScheduleConfig": {"ScheduleExpression": "cron(0 * ? * * *)"},  # a cada hora
        "MonitoringJobDefinition": {
            "BaselineConfig": {
                "ConstraintsResource": {"S3Uri": f"{BASELINE_S3}constraints.json"},
                "StatisticsResource": {"S3Uri": f"{BASELINE_S3}statistics.json"},
            },
            "MonitoringInputs": [
                {
                    "EndpointInput": {
                        "EndpointName": ENDPOINT_NAME,
                        "LocalPath": "/opt/ml/processing/input",
                    }
                }
            ],
            "MonitoringOutputConfig": {
                "MonitoringOutputs": [
                    {
                        "S3Output": {
                            "S3Uri": REPORT_S3,
                            "LocalPath": "/opt/ml/processing/output",
                        }
                    }
                ]
            },
            "MonitoringResources": {
                "ClusterConfig": {
                    "InstanceCount": 1,
                    "InstanceType": "ml.m5.xlarge",
                    "VolumeSizeInGB": 20,
                }
            },
            "MonitoringAppSpecification": {
                "ImageUri": "156813124566.dkr.ecr.us-east-1.amazonaws.com/sagemaker-model-monitor-analyzer"
            },
            "RoleArn": ROLE_ARN,
        },
    },
)
print("Monitoring schedule criado em", datetime.now().isoformat())
