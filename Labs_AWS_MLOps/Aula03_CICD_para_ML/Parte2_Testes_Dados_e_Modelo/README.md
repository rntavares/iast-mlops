# Parte 2 — Estendendo o Buildspec com Testes de Dados e Modelo

1. Substitua o `buildspec.yml` da Parte 1 pelo desta pasta (adiciona as fases `test-data` e `test-model`).
2. Copie `scripts/` para dentro do repositório `ml-ci-lab` criado na Parte 1.
3. Faça commit e push — acompanhe o CodeBuild rodando as 3 fases: `test-code`, `test-data`, `test-model`.
4. **Para ver o pipeline falhar de propósito**: abra `scripts/test_model_quality.py` e suba o `THRESHOLD_ACCURACY` para `0.99`. Push de novo e veja o build falhar no CodeBuild.
5. Corrija o threshold de volta (ex: `0.70`) e confira o build passando.

Isso mostra na prática por que "só rodar pytest" não é suficiente para ML — dados e modelo também quebram silenciosamente.
