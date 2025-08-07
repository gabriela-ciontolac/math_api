from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database.session import SessionLocal
from app.models.request_log import RequestLog
from app.schemas.math import PowRequest, PowResponse, FibonacciRequest, FibonacciResponse, FactorialRequest, FactorialResponse
from app.services.math_service import compute_power, compute_fibonacci, compute_factorial
from app.metrics.metrics import operation_counter, operation_duration
from app.services.math_service import compute_factorial_with_cache, compute_fibonacci_with_cache, compute_power_with_cache
from app.auth.auth import get_current_user
from app.logging.kafka_logger import log_event
from datetime import datetime

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/pow", response_model=PowResponse)
async def power_endpoint(payload: PowRequest, db: Session = Depends(get_db), op = "pow", username: str = Depends(get_current_user)):
    # Start measuring duration
    with operation_duration.labels(operation=op).time():
        try:
            result = await compute_power_with_cache(payload.base, payload.exp)
        except Exception as e:
            raise HTTPException(status_code=400, detail=str(e))
        
        # Increment operation counter
        operation_counter.labels(operation=op).inc()
        
        log = RequestLog(
            operation=op,
            input_data=payload.json(),
            result=result,
            username=username
        )

        db.add(log)
        db.commit()

        await log_event({
            "username": username,
            "operation": op,
            "inputs": payload.dict(),
            "result": result,
            "timestamp": str(datetime.utcnow())
        })

        return {"result": result}

@router.post("/fibonacci", response_model=FibonacciResponse)
async def fibonacci_endpoint(payload: FibonacciRequest, db: Session = Depends(get_db), op = "fibonacci", username: str = Depends(get_current_user)):
    # Start measuring duration
    with operation_duration.labels(operation=op).time():
        try:
            result = await compute_fibonacci_with_cache(payload.n)
        except Exception as e:
            raise HTTPException(status_code=400, detail=str(e))
        
        # Increment operation counter
        operation_counter.labels(operation=op).inc()
        
        log = RequestLog(
            operation=op,
            input_data=payload.json(),
            result=result,
            username=username
        )

        db.add(log)
        db.commit()

        await log_event({
            "username": username,
            "operation": op,
            "inputs": payload.dict(),
            "result": result,
            "timestamp": str(datetime.utcnow())
        })

        return {"result": result}
    
@router.post("/factorial", response_model=FactorialResponse)
async def factorial_endpoint(payload: FactorialRequest, db: Session = Depends(get_db), op = "factorial", username: str = Depends(get_current_user)):
    # Start measuring duration
    with operation_duration.labels(operation=op).time():
        try:
            result = await compute_factorial_with_cache(payload.n)
        except Exception as e:
            raise HTTPException(status_code=400, detail=str(e))
        
        # Increment operation counter
        operation_counter.labels(operation=op).inc()

        log = RequestLog(
            operation=op,
            input_data=payload.json(),
            result=result,
            username=username
        )

        db.add(log)
        db.commit()

        await log_event({
            "username": username,
            "operation": op,
            "inputs": payload.dict(),
            "result": result,
            "timestamp": str(datetime.utcnow())
        })

        return {"result": result}