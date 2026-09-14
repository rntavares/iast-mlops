# Parte 2 — Build e Push para o ECR

Pré-requisito: copie `main.py`, `requirements.txt` e `model.joblib` da Parte 1 para esta pasta antes de buildar (ou ajuste o Dockerfile para apontar pro caminho certo).

1. Criar o repositório no ECR:
   ```bash
   aws ecr create-repository --repository-name churn-api
   ```
2. Build da imagem:
   ```bash
   docker build -t churn-api .
   ```
3. Login do Docker no ECR (substitua `SUA-CONTA` e `SUA-REGIAO`):
   ```bash
   aws ecr get-login-password --region SUA-REGIAO | \
     docker login --username AWS --password-stdin SUA-CONTA.dkr.ecr.SUA-REGIAO.amazonaws.com
   ```
4. Tag e push:
   ```bash
   docker tag churn-api:latest SUA-CONTA.dkr.ecr.SUA-REGIAO.amazonaws.com/churn-api:latest
   docker push SUA-CONTA.dkr.ecr.SUA-REGIAO.amazonaws.com/churn-api:latest
   ```
5. Confirmar a imagem publicada em **ECR → Repositories → churn-api**.

Ou simplesmente rode `./build_and_push.sh SUA-CONTA SUA-REGIAO` que faz os 4 passos acima de uma vez.
