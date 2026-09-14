"""Valida schema e qualidade basica dos dados antes de treinar.
Sai com codigo != 0 (falha o build) se alguma checagem nao passar.
"""
import sys
import pandas as pd

COLUNAS_ESPERADAS = {
    "Survived", "Pclass", "Sex", "Age", "SibSp", "Parch", "Fare", "Embarked"
}


def gerar_dados_exemplo() -> pd.DataFrame:
    # em um pipeline real, isso viria de s3://.../dados.csv
    return pd.DataFrame({
        "Survived": [0, 1, 1, 0],
        "Pclass": [3, 1, 2, 3],
        "Sex": ["male", "female", "female", "male"],
        "Age": [22, 38, 26, 35],
        "SibSp": [1, 1, 0, 0],
        "Parch": [0, 0, 0, 0],
        "Fare": [7.25, 71.28, 7.92, 8.05],
        "Embarked": ["S", "C", "S", "S"],
    })


def validar(df: pd.DataFrame) -> list[str]:
    erros = []

    faltando = COLUNAS_ESPERADAS - set(df.columns)
    if faltando:
        erros.append(f"Colunas faltando: {faltando}")

    if df.empty:
        erros.append("Dataframe vazio")

    if "Age" in df.columns and (df["Age"] < 0).any():
        erros.append("Existem idades negativas")

    if "Fare" in df.columns and df["Fare"].isnull().mean() > 0.5:
        erros.append("Mais de 50% dos valores de Fare estao nulos")

    return erros


def main():
    df = gerar_dados_exemplo()
    erros = validar(df)
    if erros:
        print("FALHOU - problemas de qualidade de dados:")
        for e in erros:
            print(" -", e)
        sys.exit(1)
    print("Dados OK - todas as checagens de qualidade passaram.")


if __name__ == "__main__":
    main()
