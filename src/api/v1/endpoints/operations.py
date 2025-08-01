from fastapi import APIRouter
from database.core import get_db
from database.models import Operation
from sqlalchemy.orm import Session
from fastapi import Depends

router = APIRouter()

@router.get("/")
async def get_operations(db: Session = Depends(get_db)):

    operations = db.query(Operation).all()

    return  operations