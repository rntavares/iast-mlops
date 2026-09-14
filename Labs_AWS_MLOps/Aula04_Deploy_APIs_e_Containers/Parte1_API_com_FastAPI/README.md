# Parte 1 — API de Predição com FastAPI

1. Instalar dependências:
   ```bash
   pip install -r requirements.txt
   ```
2. Colocar um `model.joblib` treinado nesta pasta (pode reusar o da Aula 01 - Parte 1, ou rodar `python treinar_modelo_exemplo.py` para gerar um rapidinho).
3. Subir a API local:
   ```bash
   uvicorn main:app --reload --port 8000
   ```
4. Abrir **http://localhost:8000/docs** — a UI Swagger é gerada automaticamente.
5. Testar o endpoint `POST /predict` direto pela UI, e o `GET /health` (deve responder `"model_loaded": true`).
