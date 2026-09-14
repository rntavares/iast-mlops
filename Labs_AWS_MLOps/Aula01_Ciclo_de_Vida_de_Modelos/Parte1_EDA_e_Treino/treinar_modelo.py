"""
Aula 01 - Parte 1: EDA e treino de um modelo simples no SageMaker.

Pré-requisito: um CSV do dataset Titanic (colunas: Survived, Pclass, Sex, Age,
SibSp, Parch, Fare, ...) já enviado para o S3.
"""
import boto3
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report
from sklearn.model_selection import train_test_split
import joblib

BUCKET = "SEU-BUCKET-AQUI"
KEY = "dados/titanic.csv"


def carregar_dados(bucket: str, key: str) -> pd.DataFrame:
    return pd.read_csv(f"s3://{bucket}/{key}")


def eda_rapida(df: pd.DataFrame) -> None:
    print("=== INFO ===")
    print(df.info())
    print("\n=== DESCRIBE ===")
    print(df.describe())
    print("\n=== NULOS POR COLUNA ===")
    print(df.isnull().sum())


def preparar_features(df: pd.DataFrame) -> pd.DataFrame:
    df = df.copy()
    df["Age"] = df["Age"].fillna(df["Age"].median())
    df["Sex"] = df["Sex"].map({"male": 0, "female": 1})
    df["Embarked"] = df["Embarked"].fillna("S").map({"S": 0, "C": 1, "Q": 2})
    features = ["Pclass", "Sex", "Age", "SibSp", "Parch", "Fare", "Embarked"]
    return df[features].fillna(0), df["Survived"]


def treinar(X_train, y_train) -> RandomForestClassifier:
    modelo = RandomForestClassifier(n_estimators=100, random_state=42)
    modelo.fit(X_train, y_train)
    return modelo


def main():
    df = carregar_dados(BUCKET, KEY)
    eda_rapida(df)

    X, y = preparar_features(df)
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42, stratify=y
    )

    modelo = treinar(X_train, y_train)

    y_pred = modelo.predict(X_test)
    print("\n=== AVALIACAO ===")
    print("Accuracy:", accuracy_score(y_test, y_pred))
    print(classification_report(y_test, y_pred))

    joblib.dump(modelo, "model.joblib")
    print("\nModelo salvo em model.joblib")


if __name__ == "__main__":
    main()
