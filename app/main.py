from fastapi import FastAPI
from app.api import math_routes
from sqlalchemy import create_engine
from sqlalchemy.exc import OperationalError
from app.database.session import DB_URL
from prometheus_fastapi_instrumentator import Instrumentator
from fastapi import FastAPI, Depends, HTTPException
from fastapi.security import OAuth2PasswordRequestForm
from datetime import timedelta
from app.auth.auth import authenticate_user, create_access_token, get_current_user
from app.auth.config import ACCESS_TOKEN_EXPIRE_MINUTES
from app.logging.kafka_logger import start_kafka_producer, stop_kafka_producer

app = FastAPI(
    title="Math Microservice",
    description="A microservice to compute mathematical functions",
    version="1.0.0"
)

app.include_router(math_routes.router)

@app.post("/token")
def login(form_data: OAuth2PasswordRequestForm = Depends()):
    if not authenticate_user(form_data.username, form_data.password):
        raise HTTPException(status_code=401, detail="Invalid credentials")
    access_token = create_access_token(
        data={"sub": form_data.username},
        expires_delta=timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    )
    return {"access_token": access_token, "token_type": "bearer"}

engine = create_engine(DB_URL)

try:
    with engine.connect() as conn:
        print("Successfully connected to the database.")
except OperationalError as e:
    print("Database connection failed:", e)


Instrumentator().instrument(app).expose(app)

@app.on_event("startup")
async def startup_event():
    await start_kafka_producer()

@app.on_event("shutdown")
async def shutdown_event():
    await stop_kafka_producer()
