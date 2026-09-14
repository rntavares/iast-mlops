# Parte 3 — Canary Release no SageMaker

Pré-requisito: dois model packages aprovados no Model Registry (`v1` e `v2` — pode reaprovar a mesma versão duas vezes com nomes diferentes só para o exercício).

1. Rode `criar_endpoint_canary.py` — cria **um único endpoint** com duas `ProductionVariants`: 90% do tráfego para v1, 10% para v2.
2. Invoque o endpoint várias vezes (`invocar_varias_vezes.py`) e observe, pelos logs/CloudWatch, a distribuição real de tráfego entre as variantes.
3. Rode `ajustar_pesos_canary.py` para simular o avanço do canário (ex: 50/50, depois 0/100 quando a v2 ganhar confiança).
4. Não esqueça de deletar o endpoint ao final (mesmo passo da Aula 01 - Parte 3).
