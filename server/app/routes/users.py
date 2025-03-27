from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from services import user_services
from schemas import schema_user
from database.database import get_db

router = APIRouter(prefix="/users", tags=["Users"])


@router.post("/", response_model=schema_user.UserResponse)
def create_user(user: schema_user.UserCreate, db: Session = Depends(get_db)):
    db_user = user_services.create_user(db, user)
    return db_user


@router.get("/", response_model=list[schema_user.UserResponse])
def read_users(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    return user_services.get_users(db, skip, limit)


@router.get("/{user_id}", response_model=schema_user.UserResponse)
def read_user(user_id: int, db: Session = Depends(get_db)):
    user = user_services.get_user(db, user_id)
    if user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return user


@router.put("/{user_id}", response_model=schema_user.UserResponse)
def update_user(
    user_id: int, user: schema_user.UserCreate, db: Session = Depends(get_db)
):
    updated_user = user_services.update_user(db, user_id, user)
    if updated_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return updated_user


@router.delete("/{user_id}")
def delete_user(user_id: int, db: Session = Depends(get_db)):
    deleted_user = user_services.delete_user(db, user_id)
    if deleted_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return {"message": "User deleted successfully"}
