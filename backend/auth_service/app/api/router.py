from fastapi import APIRouter, status

from backend.auth_service.app.api.schemas import RegisterInput
from backend.auth_service.app.db.crud import create_user

router = APIRouter(
    prefix="/accounts",
    tags=["accounts"],
    # dependencies=[Depends(get_token_header)],
    responses={404: {"description": "Not found"}},
)


@router.post("/register", status_code=status.HTTP_201_CREATED)
async def register(user: RegisterInput):
    db_user = await create_user(user_create=user)
    return db_user
