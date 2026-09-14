"""Gera um model.joblib de exemplo, caso voce nao tenha o da Aula 01."""
import joblib
from sklearn.datasets import make_classification
from sklearn.ensemble import RandomForestClassifier

X, y = make_classification(n_samples=500, n_features=7, random_state=42)
modelo = RandomForestClassifier(n_estimators=100, random_state=42)
modelo.fit(X, y)
joblib.dump(modelo, "model.joblib")
print("model.joblib gerado.")
