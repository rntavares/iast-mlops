"""Aula 02 - Parte 3: promove a ultima versao registrada por Staging -> Production."""
from mlflow.tracking import MlflowClient
import mlflow

TRACKING_SERVER_ARN = "arn:aws:sagemaker:us-east-1:SUA-CONTA:mlflow-tracking-server/SEU-SERVER"
MODEL_NAME = "churn-model"

mlflow.set_tracking_uri(TRACKING_SERVER_ARN)
client = MlflowClient()

versoes = client.search_model_versions(f"name='{MODEL_NAME}'")
if not versoes:
    raise SystemExit("Nenhuma versao encontrada - rode registrar_modelo.py primeiro.")

ultima = max(versoes, key=lambda v: int(v.version))
print(f"Promovendo {MODEL_NAME} v{ultima.version}...")

# 1. move para Staging
client.transition_model_version_stage(
    name=MODEL_NAME, version=ultima.version, stage="Staging"
)
print("-> Staging")

# 2. "validacao" simulada: checa se a metrica de accuracy do run e boa o suficiente
run = client.get_run(ultima.run_id)
accuracy = run.data.metrics.get("accuracy", 0)
print(f"Accuracy do run: {accuracy:.3f}")

if accuracy >= 0.75:
    client.transition_model_version_stage(
        name=MODEL_NAME, version=ultima.version, stage="Production"
    )
    print("-> Production (accuracy acima do threshold)")
else:
    print("Modelo NAO promovido - accuracy abaixo do threshold de 0.75")
