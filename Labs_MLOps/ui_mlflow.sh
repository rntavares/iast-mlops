#!/bin/bash
# Sobe a interface do MLflow (porta 5000) com o banco compartilhado pelos labs.
# O MLflow 3 bloqueia (HTTP 403) acessos que não venham de localhost; no
# Codespaces o navegador chega por um endereço *.app.github.dev, então é
# preciso liberá-lo explicitamente.
cd "$(dirname "$0")"
mlflow ui \
  --backend-store-uri sqlite:///mlflow.db \
  --port 5000 \
  --allowed-hosts "*.app.github.dev,localhost,127.0.0.1" \
  --cors-allowed-origins "https://*.app.github.dev"
