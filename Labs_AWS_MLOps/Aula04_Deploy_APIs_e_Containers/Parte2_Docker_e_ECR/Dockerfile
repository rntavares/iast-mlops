# Estagio 1: builder - instala dependencias
FROM python:3.11-slim AS builder
WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir --prefix=/install -r requirements.txt

# Estagio 2: imagem final, enxuta
FROM python:3.11-slim
WORKDIR /app

# usuario nao-root (boa pratica de seguranca)
RUN useradd --create-home appuser
COPY --from=builder /install /usr/local
COPY . .
RUN chown -R appuser:appuser /app
USER appuser

EXPOSE 8000

HEALTHCHECK --interval=30s --timeout=5s --start-period=10s \
  CMD python -c "import urllib.request; urllib.request.urlopen('http://localhost:8000/health')" || exit 1

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
