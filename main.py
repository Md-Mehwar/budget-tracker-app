from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from sqlalchemy import text
from database import SessionLocal

app = FastAPI()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/")
def home():
    return {"message": "Backend is running!"}

@app.get("/test-db")
def test_db_connection(db: Session = Depends(get_db)):
    try:
        db.execute(text("SELECT 1"))
        return {"status": "Database connected successfully!"}
    except Exception as e:
        return {"status": "Failed to connect", "error": str(e)}
from database import Base, engine
import models

# Create tables
Base.metadata.create_all(bind=engine)

