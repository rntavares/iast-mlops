# Parte 1 — CI com CodeCommit e CodeBuild

1. Criar o repositório:
   ```bash
   aws codecommit create-repository --repository-name ml-ci-lab
   ```
2. Clonar o repositório vazio e copiar os arquivos desta pasta (`src/`, `tests/`, `buildspec.yml`) para dentro dele:
   ```bash
   git clone https://git-codecommit.SUA-REGIAO.amazonaws.com/v1/repos/ml-ci-lab
   cp -r src tests buildspec.yml ml-ci-lab/
   cd ml-ci-lab && git add . && git commit -m "commit inicial" 
   ```
3. Criar o projeto no CodeBuild apontando para esse repositório (Source = CodeCommit, Environment = imagem gerenciada `aws/codebuild/standard:7.0`, Buildspec = usar o arquivo do repo).
4. Configurar um trigger de webhook para rodar o build a cada push (CodeBuild → seu projeto → Edit → Source → "Rebuild every time a code change is pushed").
5. `git push` e acompanhar o build em **CodeBuild → Build history**.

O `buildspec.yml` roda `pytest tests/` — se o teste falhar, o build falha.
