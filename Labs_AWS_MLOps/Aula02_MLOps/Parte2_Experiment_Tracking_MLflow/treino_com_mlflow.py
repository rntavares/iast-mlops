"""Aula 02 - Parte 2: treina um modelo e loga o experimento no MLflow
(tracking server gerenciado pelo SageMaker)."""
import mlflow
import mlflow.sklearn
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, f1_score
from sklearn.model_selection import train_test_split

TRACKING_SERVER_ARN = "arn:aws:sagemaker:us-east-1:SUA-CONTA:mlflow-tracking-server/SEU-SERVER"
EXPERIMENT_NAME = "previsao-churn"

N_ESTIMATORS = 150
MAX_DEPTH = 8


def carregar_dados_exemplo():
    # troque por pd.read_csv("s3://.../dados.csv") com o seu dataset real
    from sklearn.datasets import make_classification

    X, y = make_classification(n_samples=2000, n_features=10, random_state=42)
    return pd.DataFrame(X), pd.Series(y)


def main():
    mlflow.set_tracking_uri(TRACKING_SERVER_ARN)
    mlflow.set_experiment(EXPERIMENT_NAME)

    X, y = carregar_dados_exemplo()
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42
    )

    with mlflow.start_run():
        mlflow.log_param("n_estimators", N_ESTIMATORS)
        mlflow.log_param("max_depth", MAX_DEPTH)

        modelo = RandomForestClassifier(
            n_estimators=N_ESTIMATORS, max_depth=MAX_DEPTH, random_state=42
        )
        modelo.fit(X_train, y_train)

        y_pred = modelo.predict(X_test)
        acc = accuracy_score(y_test, y_pred)
        f1 = f1_score(y_test, y_pred)

        mlflow.log_metric("accuracy", acc)
        mlflow.log_metric("f1_score", f1)

        mlflow.sklearn.log_model(modelo, "model")

        print(f"Run registrado. accuracy={acc:.3f} f1={f1:.3f}")


if __name__ == "__main__":
    main()
