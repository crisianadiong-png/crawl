from fastapi import FastAPI
from sqlalchemy import text

from database import Base, engine
import models


Base.metadata.create_all(bind=engine)


app = FastAPI(
    title="Personal Finance Tracker API",
    description="Backend API for the Personal Finance Tracker",
    version="1.0.0"
)


@app.get("/")
def root():
    return {
        "message": "Personal Finance Tracker API is running!"
    }


@app.get("/health")
def health_check():
    try:
        with engine.connect() as connection:
            connection.execute(text("SELECT 1"))

        return {
            "status": "healthy",
            "database": "connected"
        }

    except Exception as error:
        return {
            "status": "unhealthy",
            "database": "disconnected",
            "error": str(error)
        }