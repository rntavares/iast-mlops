"""Aula 03 - Parte 3: invoca o endpoint canary repetidas vezes e conta
quantas respostas vieram de cada variante (via header retornado)."""
import boto3
from collections import Counter

runtime = boto3.client("sagemaker-runtime")

ENDPOINT_NAME = "churn-canary-endpoint"
N_CHAMADAS = 50
payload = "3,0,22,1,0,7.25,0"

contagem = Counter()
for _ in range(N_CHAMADAS):
    resp = runtime.invoke_endpoint(
        EndpointName=ENDPOINT_NAME, ContentType="text/csv", Body=payload
    )
    variante = resp["InvokedProductionVariant"]
    contagem[variante] += 1

print(f"Distribuicao de trafego em {N_CHAMADAS} chamadas:")
for variante, qtd in contagem.items():
    print(f"  {variante}: {qtd} ({qtd / N_CHAMADAS:.0%})")
