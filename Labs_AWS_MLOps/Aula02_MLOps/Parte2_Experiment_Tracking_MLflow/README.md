# Parte 2 — Experiment Tracking com MLflow

1. No console: **SageMaker → MLflow → Create tracking server** (fica pronto em alguns minutos).
2. Instalar as dependências:
   ```bash
   pip install -r requirements.txt
   ```
3. Editar `TRACKING_SERVER_ARN` em `treino_com_mlflow.py` com o ARN do tracking server criado no passo 1.
4. Rodar:
   ```bash
   python treino_com_mlflow.py
   ```
5. Abrir a UI do MLflow (botão "Open MLflow" no console do tracking server) e comparar as execuções — parâmetros, métricas e o artefato do modelo logado.

Rode o script 2-3 vezes mudando `N_ESTIMATORS` para ter mais de uma execução pra comparar.
