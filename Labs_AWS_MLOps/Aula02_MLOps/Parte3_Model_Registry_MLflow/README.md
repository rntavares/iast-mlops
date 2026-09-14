# Parte 3 — Promovendo um Modelo no MLflow Model Registry

1. Rode `registrar_modelo.py` para pegar o último run da Parte 2 e registrá-lo no Model Registry do MLflow.
2. Rode `promover_modelo.py` para mover a versão registrada por `None → Staging → Production`.
3. Abra a UI do MLflow e confira, na aba **Models**, o histórico de transições de estágio da versão.

Isso reproduz o fluxo real: cientista treina → registra → promove após validação.
