"""Aula 04 - Parte 1: API de predicao com FastAPI + Pydantic."""
from contextlib import asynccontextmanager

import joblib
from fastapi import FastAPI
from pydantic import BaseModel, Field

modelo = None


@asynccontextmanager
async def lifespan(app: FastAPI):
    global modelo
    # carrega o modelo UMA vez, na inicializacao - nao a cada requisicao
    modelo = joblib.load("model.joblib")
    yield


app = FastAPI(title="API de Predicao de Churn", lifespan=lifespan)


class PredictionInput(BaseModel):
    pclass: int = Field(..., ge=1, le=3, description="Classe do passageiro (1-3)")
    sex: int = Field(..., ge=0, le=1, description="0=masculino, 1=feminino")
    age: float = Field(..., ge=0, le=120)
    sibsp: int = Field(..., ge=0)
    parch: int = Field(..., ge=0)
    fare: float = Field(..., ge=0)
    embarked: int = Field(..., ge=0, le=2, description="0=S, 1=C, 2=Q")


class PredictionOutput(BaseModel):
    prediction: int
    probability: float


@app.get("/health")
def health():
    return {"status": "ok", "model_loaded": modelo is not None}


@app.post("/predict", response_model=PredictionOutput)
def predict(payload: PredictionInput):
    features = [[
        payload.pclass, payload.sex, payload.age,
        payload.sibsp, payload.parch, payload.fare, payload.embarked,
    ]]
    pred = modelo.predict(features)[0]
    proba = modelo.predict_proba(features)[0][1]
    return PredictionOutput(prediction=int(pred), probability=float(proba))
