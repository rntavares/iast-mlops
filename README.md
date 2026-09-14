# 🚀 FIAP — Pós-Graduação IAST: MLOps
### Deploy, Automação, CI/CD e Monitoramento de Modelos de Machine Learning na AWS

Repositório central de materiais, apresentações, documentação técnica e laboratórios práticos da disciplina de **MLOps** do curso de **Pós-Graduação em Inteligência Artificial para Soluções Tecnológicas (IAST)** da **FIAP**.

---

## 🎯 Visão Geral da Disciplina

O objetivo desta disciplina é capacitar engenheiros e cientistas de dados a levar modelos de Machine Learning do ambiente de experimentação para a produção de forma escalável, segura e automatizada. Durante as aulas, são explorados conceitos fundamentais e avançados de MLOps utilizando o ecossistema da **AWS (Amazon Web Services)** e ferramentas modernas de mercado (MLflow, Docker, FastAPI, CI/CD).

```
 ┌─────────────┐     ┌──────────────┐     ┌─────────────┐     ┌─────────────┐
 │   AULA 01   │ ──▶ │   AULA 02    │ ──▶ │   AULA 03   │ ──▶ │   AULA 04   │
 │Ciclo de Vida│     │  MLOps com   │     │ CI/CD para  │     │ Deploy APIs │
 │ & SageMaker │     │ MLflow & AWS │     │     ML      │     │& Containers │
 └─────────────┘     └──────────────┘     └─────────────┘     └─────────────┘
```

---

## 📂 Estrutura do Repositório

```text
MLOps/
├── 📚 Docs-Aulas-MLOps/            # Apostilas, capítulos teóricos e desafios
│   ├── capitulos/                  # Documentos detalhados de cada aula (01 a 04)
│   ├── desafio/                    # Especificação do Desafio Final Integrado
│   └── roteiros/                   # Planejamento e roteiro pedagógico
│
├── 🛠️ Labs_AWS_MLOps/              # Laboratórios práticos (12 labs mão na massa)
│   ├── Aula01_Ciclo_de_Vida_de_Modelos/
│   │   ├── Parte1_EDA_e_Treino/
│   │   ├── Parte2_Model_Registry/
│   │   └── Parte3_Deploy_e_Monitor/
│   ├── Aula02_MLOps/
│   │   ├── Parte1_Explorando_o_SageMaker/
│   │   ├── Parte2_Experiment_Tracking_MLflow/
│   │   └── Parte3_Model_Registry_MLflow/
│   ├── Aula03_CICD_para_ML/
│   │   ├── Parte1_CI_CodeCommit_CodeBuild/
│   │   ├── Parte2_Testes_Dados_e_Modelo/
│   │   └── Parte3_Canary_Release/
│   └── Aula04_Deploy_APIs_e_Containers/
│       ├── Parte1_API_com_FastAPI/
│       ├── Parte2_Docker_e_ECR/
│       └── Parte3_App_Runner/
│
└── 📊 PPTs-Aulas-MLOps/            # Slides e apresentações (PowerPoint)
    ├── Aula01_Ciclo_de_Vida_de_Modelos.pptx
    ├── Aula02_MLOps.pptx
    ├── Aula03_CICD_Machine_Learning.pptx
    └── Aula04_Deploy_APIs_Containers.pptx
```

---

## 📖 Trilha de Aprendizagem & Conteúdo das Aulas

### 🔹 Aula 01 — Ciclo de Vida de Modelos e Fundamentos na Nuvem
* **Teoria:** Da exploração dos dados à produção: desafios do ciclo de vida tradicional vs. MLOps, governança e versionamento.
* **Labs Práticos (`Labs_AWS_MLOps/Aula01_...`):**
  * `Parte 1`: Análise Exploratória (EDA) e treinamento de modelo baseline.
  * `Parte 2`: Registro e versionamento de modelos no Amazon SageMaker Model Registry.
  * `Parte 3`: Deploy em tempo real com SageMaker Endpoints e monitoramento básico.

### 🔹 Aula 02 — MLOps, Rastreabilidade e Gestão de Experimentos
* **Teoria:** Experiment Tracking, reprodutibilidade, comparação de hiperparâmetros e arquiteturas de MLflow integradas à nuvem.
* **Labs Práticos (`Labs_AWS_MLOps/Aula02_...`):**
  * `Parte 1`: Navegação e recursos do Amazon SageMaker Studio.
  * `Parte 2`: Rastreamento de experimentos com MLflow (métricas, artefatos, parâmetros).
  * `Parte 3`: Gestão de ciclo de vida e transição de estágios no MLflow Model Registry.

### 🔹 Aula 03 — CI/CD para Machine Learning (CT/CD)
* **Teoria:** Integração e Entrega Contínuas aplicadas a dados e modelos, validação automatizada de drift e estratégias de rollout (Canary, Blue/Green).
* **Labs Práticos (`Labs_AWS_MLOps/Aula03_...`):**
  * `Parte 1`: Criação de pipeline automatizado com AWS CodeCommit e AWS CodeBuild.
  * `Parte 2`: Implementação de testes automatizados de dados (schema/data quality) e validação de performance do modelo.
  * `Parte 3`: Estratégia de deploy Canary Release com divisão de tráfego.

### 🔹 Aula 04 — Deploy de APIs, Conteinerização e Serverless
* **Teoria:** Microsserviços de inferência, conteinerização com Docker, orquestração e deploy serverless em escala.
* **Labs Práticos (`Labs_AWS_MLOps/Aula04_...`):**
  * `Parte 1`: Construção de API de inferência de alta performance com FastAPI.
  * `Parte 2`: Empacotamento em imagem Docker e publicação no Amazon ECR (Elastic Container Registry).
  * `Parte 3`: Deploy serverless e escalável com AWS App Runner.

---

## 🛠️ Pré-requisitos & Ambiente de Desenvolvimento

Para reproduzir os laboratórios práticos, você precisará:

1. **Conta AWS:**
   * Conta ativa com acesso aos serviços utilizados (SageMaker, S3, ECR, CodeBuild, App Runner).
2. **AWS CLI:**
   * Instalado e autenticado localmente (`aws configure`).
3. **Ambiente Python:**
   * Python 3.10 ou superior.
   * Criação recomendada de ambiente virtual (`python -m venv .venv`).
4. **Docker:**
   * Docker Desktop ou Docker Engine instalado (necessário para a Aula 04).

---

## ⚠️ Gerenciamento de Custos na AWS

> **IMPORTANTE:** Alguns serviços da AWS geram cobrança contínua enquanto estiverem ativos (ex: *SageMaker Real-time Endpoints* e instâncias do *App Runner*).
> 
> * Sempre execute o passo de **cleanup / exclusão de recursos** descrito ao final de cada `README.md` dos laboratórios.
> * Monitore o painel de **AWS Cost Explorer** e configure alertas de faturamento (*CloudWatch Billing Alarms*).

---

## 🏆 Desafio Final Integrado

O diretório `Docs-Aulas-MLOps/desafio/` contém a especificação do **Desafio Final Integrado**, onde os alunos consolidam todo o conhecimento da disciplina construindo um pipeline de MLOps completo de ponta a ponta.

---

## 👨‍🏫 Autor & Coordenação

* **Curso:** Pós-Graduação em Inteligência Artificial para Soluções Tecnológicas (IAST)
* **Instituição:** [FIAP](https://www.fiap.com.br)
