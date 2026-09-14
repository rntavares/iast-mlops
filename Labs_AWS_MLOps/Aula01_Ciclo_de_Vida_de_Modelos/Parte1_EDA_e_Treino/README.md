# Parte 1 — EDA e Treino no SageMaker

1. Criar um bucket S3 e subir o dataset (Titanic é um bom exemplo pequeno e público):
   ```bash
   aws s3 mb s3://SEU-BUCKET-AQUI
   aws s3 cp titanic.csv s3://SEU-BUCKET-AQUI/dados/titanic.csv
   ```
2. Abra o SageMaker Studio → crie um notebook novo com o kernel **Data Science**.
3. Suba `treinar_modelo.py` (ou cole o conteúdo célula a célula) e ajuste o valor de `BUCKET`.
4. Rode o script. Ele faz: carga do CSV do S3 → EDA rápida → treino de um `RandomForestClassifier` → avaliação → salva `model.joblib` localmente.
5. Confira a accuracy impressa no final — é o baseline que vamos empacotar na Parte 2.

## Rodando localmente (sem Studio)

```bash
pip install -r requirements.txt
python treinar_modelo.py
```
