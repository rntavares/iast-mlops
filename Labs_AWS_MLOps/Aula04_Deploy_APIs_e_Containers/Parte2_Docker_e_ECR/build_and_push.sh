#!/usr/bin/env bash
# Uso: ./build_and_push.sh <conta-aws> <regiao>
set -euo pipefail

CONTA="${1:?Informe a conta AWS. Uso: ./build_and_push.sh <conta-aws> <regiao>}"
REGIAO="${2:?Informe a regiao. Uso: ./build_and_push.sh <conta-aws> <regiao>}"
REPO="churn-api"
URL="${CONTA}.dkr.ecr.${REGIAO}.amazonaws.com/${REPO}"

aws ecr describe-repositories --repository-names "$REPO" --region "$REGIAO" >/dev/null 2>&1 \
  || aws ecr create-repository --repository-name "$REPO" --region "$REGIAO"

docker build -t "$REPO" .

aws ecr get-login-password --region "$REGIAO" \
  | docker login --username AWS --password-stdin "${CONTA}.dkr.ecr.${REGIAO}.amazonaws.com"

docker tag "${REPO}:latest" "${URL}:latest"
docker push "${URL}:latest"

echo "Imagem publicada em: ${URL}:latest"
