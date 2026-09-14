# Labs AWS — Deploy e Monitoramento de Modelos de ML

Um laboratório por parte de aula (12 no total), pensados para 15–20 min cada.

## Pré-requisitos gerais

- Conta AWS com Free Tier (ou orçamento pequeno — alguns labs saem de graça, outros custam centavos se você não esquecer de derrubar os recursos)
- AWS CLI instalado e configurado (`aws configure`)
- Python 3.10+
- Docker instalado (só necessário na Aula 04)
- IAM: para simplificar em sala de aula, use um usuário/role com `AmazonSageMakerFullAccess`, `AmazonS3FullAccess`, `AmazonEC2ContainerRegistryFullAccess`, `AWSCodeBuildAdminAccess` e `AWSCodeCommitFullAccess`. Em produção, troque por políticas com escopo mínimo.

## ⚠️ Atenção a custos

Os labs que criam um **SageMaker Endpoint** (Aula01-Parte3, Aula03-Parte3) e o **App Runner** (Aula04-Parte3) cobram por hora enquanto o recurso existir. Cada README desses labs termina com o passo de exclusão — não pule.

## Estrutura

```
Aula01_Ciclo_de_Vida_de_Modelos/
  Parte1_EDA_e_Treino/
  Parte2_Model_Registry/
  Parte3_Deploy_e_Monitor/

Aula02_MLOps/
  Parte1_Explorando_o_SageMaker/
  Parte2_Experiment_Tracking_MLflow/
  Parte3_Model_Registry_MLflow/

Aula03_CICD_para_ML/
  Parte1_CI_CodeCommit_CodeBuild/
  Parte2_Testes_Dados_e_Modelo/
  Parte3_Canary_Release/

Aula04_Deploy_APIs_e_Containers/
  Parte1_API_com_FastAPI/
  Parte2_Docker_e_ECR/
  Parte3_App_Runner/
```

Cada pasta de parte tem seu próprio `README.md` com o passo a passo — são os mesmos passos que estão nos slides "LAB PRÁTICO", só que com o código pronto pra copiar e colar.
