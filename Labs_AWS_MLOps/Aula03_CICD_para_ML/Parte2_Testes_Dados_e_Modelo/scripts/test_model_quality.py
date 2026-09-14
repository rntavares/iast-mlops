"""Treina rapidamente e checa se a accuracy supera um threshold minimo.
Sai com codigo != 0 (falha o build) se o modelo nao atingir o threshold.
"""
import sys
from sklearn.datasets import make_classification
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split

THRESHOLD_ACCURACY = 0.70


def main():
    X, y = make_classification(n_samples=500, n_features=10, random_state=42)
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42
    )

    modelo = RandomForestClassifier(n_estimators=100, random_state=42)
    modelo.fit(X_train, y_train)
    acc = accuracy_score(y_test, modelo.predict(X_test))

    print(f"Accuracy obtida: {acc:.3f} (threshold: {THRESHOLD_ACCURACY})")

    if acc < THRESHOLD_ACCURACY:
        print("FALHOU - accuracy abaixo do threshold minimo.")
        sys.exit(1)

    print("Modelo OK - accuracy acima do threshold.")


if __name__ == "__main__":
    main()
