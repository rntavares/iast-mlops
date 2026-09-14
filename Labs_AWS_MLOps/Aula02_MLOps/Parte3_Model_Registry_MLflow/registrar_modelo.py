"""Aula 02 - Parte 3: registra o modelo do ultimo run no Model Registry do MLflow."""
import mlflow
from mlflow.tracking import MlflowClient

TRACKING_SERVER_ARN = "arn:aws:sagemaker:us-east-1:SUA-CONTA:mlflow-tracking-server/SEU-SERVER"
EXPERIMENT_NAME = "previsao-churn"
MODEL_NAME = "churn-model"

mlflow.set_tracking_uri(TRACKING_SERVER_ARN)
client = MlflowClient()

experiment = client.get_experiment_by_name(EXPERIMENT_NAME)
runs = client.search_runs(
    experiment_ids=[experiment.experiment_id],
    order_by=["start_time DESC"],
    max_results=1,
)
if not runs:
    raise SystemExit("Nenhum run encontrado - rode o treino da Parte 2 primeiro.")

run_id = runs[0].info.run_id
model_uri = f"runs:/{run_id}/model"

resultado = mlflow.register_model(model_uri, MODEL_NAME)
print(f"Modelo registrado: {MODEL_NAME} versao {resultado.version}")
