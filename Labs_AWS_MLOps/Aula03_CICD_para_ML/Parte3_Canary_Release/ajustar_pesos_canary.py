"""Aula 03 - Parte 3: ajusta os pesos de trafego entre as variantes
(simula o avanco gradual do canario: 90/10 -> 50/50 -> 0/100)."""
import boto3
import sys

sm = boto3.client("sagemaker")

ENDPOINT_NAME = "churn-canary-endpoint"


def ajustar(peso_principal: int, peso_canario: int):
    sm.update_endpoint_weights_and_capacities(
        EndpointName=ENDPOINT_NAME,
        DesiredWeightsAndCapacities=[
            {"VariantName": "Principal", "DesiredWeight": peso_principal},
            {"VariantName": "Canario", "DesiredWeight": peso_canario},
        ],
    )
    print(f"Pesos atualizados: Principal={peso_principal} Canario={peso_canario}")


if __name__ == "__main__":
    # exemplo de uso: python ajustar_pesos_canary.py 50 50
    if len(sys.argv) == 3:
        ajustar(int(sys.argv[1]), int(sys.argv[2]))
    else:
        print("Uso: python ajustar_pesos_canary.py <peso_principal> <peso_canario>")
        print("Exemplo: python ajustar_pesos_canary.py 50 50")
