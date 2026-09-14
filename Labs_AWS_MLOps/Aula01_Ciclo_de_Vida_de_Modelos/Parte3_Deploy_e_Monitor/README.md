# Parte 3 — Deploy e Model Monitor

1. Deploy do modelo aprovado na Parte 2 como endpoint real-time:
   ```bash
   python deploy_endpoint.py
   ```
   (leva ~5-8 min para o endpoint ficar `InService`)
2. Invocar o endpoint com um payload de teste:
   ```bash
   python invocar_endpoint.py
   ```
3. Habilitar o Data Capture e criar o Monitoring Schedule (Model Monitor - Data Quality):
   ```bash
   python criar_monitoring_schedule.py
   ```
4. **Ao final da aula, derrube o endpoint** (ele cobra por hora rodando):
   ```bash
   python deletar_endpoint.py
   ```

## Custo

`ml.t2.medium` é elegível a Free Tier nos primeiros meses de conta nova; fora do Free Tier, sai por poucos centavos por hora. O importante é não deixar rodando.
