# Parte 2 — Model Registry na AWS

1. Empacotar o modelo treinado na Parte 1:
   ```bash
   tar -czf model.tar.gz model.joblib
   aws s3 cp model.tar.gz s3://SEU-BUCKET-AQUI/models/v1/model.tar.gz
   ```
2. Rode `criar_model_package_group.py` uma vez (cria o "grupo" — o container lógico das versões do modelo).
3. Rode `registrar_model_package.py` para registrar essa versão específica, apontando para o artefato no S3.
4. Aprove manualmente (simulando um gate de qualidade humano):
   ```bash
   python aprovar_model_package.py
   ```
5. Confira no console: **SageMaker → Model Registry → churn-model-group** — a versão deve aparecer como `Approved`.

Alternativa 100% console: Studio → Models → Model groups → Create model group → Create version, preenchendo o caminho do S3 na tela.
