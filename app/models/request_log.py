from sqlalchemy import Column, Integer, String, Float, DateTime, func, PrimaryKeyConstraint
from app.database.session import Base

class RequestLog(Base):
    __tablename__ = "request_logs"

    id = Column(Integer, primary_key=True, index=True)
    operation = Column(String, nullable=False)       # e.g., "pow", "fibonacci", "factorial"
    input_data = Column(String, nullable=False)      # e.g., JSON string like '{"base":2,"exp":3}'
    result = Column(Float, nullable=False)
    timestamp = Column(DateTime(timezone=True), server_default=func.now())  
    username = Column(String, nullable=True)