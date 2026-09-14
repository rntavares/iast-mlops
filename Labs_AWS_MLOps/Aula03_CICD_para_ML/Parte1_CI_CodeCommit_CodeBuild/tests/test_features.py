"""Testes unitarios da funcao de feature engineering."""
import pandas as pd
import sys
import os

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "src"))
from features import preparar_features


def _df_exemplo():
    return pd.DataFrame({
        "Pclass": [3, 1],
        "Sex": ["male", "female"],
        "Age": [22, None],
        "SibSp": [1, 0],
        "Parch": [0, 0],
        "Fare": [7.25, 71.28],
        "Embarked": ["S", None],
    })


def test_preparar_features_nao_tem_nulos():
    df = _df_exemplo()
    resultado = preparar_features(df)
    assert resultado.isnull().sum().sum() == 0


def test_sex_vira_numerico():
    df = _df_exemplo()
    resultado = preparar_features(df)
    assert resultado["Sex"].dtype != object
    assert set(resultado["Sex"].unique()).issubset({0, 1})


def test_colunas_esperadas():
    df = _df_exemplo()
    resultado = preparar_features(df)
    esperado = {"Pclass", "Sex", "Age", "SibSp", "Parch", "Fare", "Embarked"}
    assert set(resultado.columns) == esperado
