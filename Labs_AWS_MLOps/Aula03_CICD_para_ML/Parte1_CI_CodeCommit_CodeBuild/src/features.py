"""Funcoes de feature engineering usadas pelo pipeline de treino."""
import pandas as pd


def preparar_features(df: pd.DataFrame) -> pd.DataFrame:
    """Recebe o dataframe cru do Titanic e devolve as features prontas para o modelo."""
    df = df.copy()
    df["Age"] = df["Age"].fillna(df["Age"].median())
    df["Sex"] = df["Sex"].map({"male": 0, "female": 1})
    df["Embarked"] = df["Embarked"].fillna("S").map({"S": 0, "C": 1, "Q": 2})
    colunas = ["Pclass", "Sex", "Age", "SibSp", "Parch", "Fare", "Embarked"]
    return df[colunas].fillna(0)
