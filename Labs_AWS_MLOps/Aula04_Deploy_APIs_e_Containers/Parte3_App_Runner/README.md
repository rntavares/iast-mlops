# Parte 3 — Publicando com App Runner

100% console (App Runner não precisa de Kubernetes nem de gerenciar cluster).

1. Console → **App Runner → Create service**.
2. Repository type: **Container registry** → Provider: **Amazon ECR** → selecione a imagem `churn-api:latest` publicada na Parte 2.
3. Deployment trigger: **Automatic** (redeploy a cada push de imagem nova).
4. Em **Configure service**:
   - Port: `8000`
   - CPU / Memória: `1 vCPU / 2 GB` (suficiente para o lab)
5. Em **Auto scaling**: min 1 instância, max 3 instâncias.
6. **Create & deploy** — aguarde o status `Running` (alguns minutos).
7. Abra a **Default domain** gerada e acesse `/docs` — a mesma API da Parte 1, agora pública e com auto-scaling, sem gerenciar servidor nenhum.
8. **Ao final, delete o serviço** (App Runner → seu serviço → Actions → Delete) para não gerar custo contínuo.

`apprunner.yaml` neste diretório é opcional — só é necessário se você quiser usar o modo "Source code" do App Runner em vez de "Container registry" (aqui usamos imagem do ECR, então o arquivo serve como referência de configuração equivalente).
