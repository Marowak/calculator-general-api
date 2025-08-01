from fastapi import APIRouter

from .endpoints import users
from .endpoints import operations
from .endpoints import records

router = APIRouter()
router.include_router(users.router, prefix="/users", tags=["Users"])
router.include_router(operations.router, prefix="/operations", tags=["Operations"])
router.include_router(records.router, prefix="/records", tags=["Records"])