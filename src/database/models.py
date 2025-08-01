from sqlalchemy import Column, Integer, String, Numeric, ForeignKey, DateTime, Boolean, func, Text
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, nullable=False, index=True)
    password = Column(Text, nullable=False) 
    status = Column(String, nullable=False, default="A")

    records = relationship("Record", back_populates="user")


class Operation(Base):
    __tablename__ = "operations"

    id = Column(Integer, primary_key=True, index=True)
    type = Column(String, nullable=False, unique=True)
    cost = Column(Numeric(10, 2), nullable=False)

    records = relationship("Record", back_populates="operation")


class Record(Base):
    __tablename__ = "records"

    id = Column(Integer, primary_key=True, index=True)
    operation_id = Column(Integer, ForeignKey("operations.id"), nullable=False)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    amount = Column(Numeric(20, 10), nullable=False)  
    user_balance = Column(Numeric(10, 2), nullable=False)
    operation_response = Column(Text, nullable=False) 
    date = Column(DateTime(timezone=True), server_default=func.now())
    deleted = Column(DateTime(timezone=True))

    user = relationship("User", back_populates="records")
    operation = relationship("Operation", back_populates="records")