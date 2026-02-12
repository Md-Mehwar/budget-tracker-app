from pydantic import BaseModel
from datetime import datetime


# ---------- USERS ----------

class UserCreate(BaseModel):
    name: str
    email: str
    password: str


class UserLogin(BaseModel):
    email: str
    password: str


class UserResponse(BaseModel):
    id: int
    name: str
    email: str

    class Config:
        orm_mode = True


class TokenResponse(BaseModel):
    access_token: str
    token_type: str


# ---------- EXPENSES ----------

class ExpenseCreate(BaseModel):
    title: str
    amount: float
    category: str


class ExpenseResponse(ExpenseCreate):
    id: int
    created_at: datetime

    class Config:
        orm_mode = True
