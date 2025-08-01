from pydantic import BaseModel, constr, condecimal
from datetime import datetime
from decimal import Decimal

# ----- User Schemas -----

class UserLogin(BaseModel):
    username: str
    password: str

    class Config:
        orm_mode = True

# ----- Operation Schemas -----

class OperationBase(BaseModel):
    type: str
    cost: Decimal

    class Config:
        orm_mode = True


# ----- Record Schemas -----

class RecordBase(BaseModel):
    operation_id: int
    user_id: int
    amount: Decimal
    user_balance: Decimal
    operation_response: str
    date: datetime

    class Config:
        orm_mode = True
