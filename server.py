from fastapi import FastAPI, Depends, HTTPException, Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
from fastapi.exceptions import RequestValidationError
from sqlalchemy.orm import Session
import uvicorn
import os

# Import database configuration
from src.config.db import get_db, Base, engine

# Import routers
from src.users.user_routes import router as user_router

# Import error handler
from src.users.core.error_handler import format_error_response, format_validation_error_response

# Create database tables
Base.metadata.create_all(bind=engine)

app = FastAPI(title="Expense Tracker API")

# Custom exception handler for HTTPException
@app.exception_handler(HTTPException)
async def http_exception_handler(request: Request, exc: HTTPException):
    return JSONResponse(
        status_code=exc.status_code,
        content=format_error_response(exc.status_code, exc.detail)
    )

# Custom exception handler for validation errors
@app.exception_handler(RequestValidationError)
async def validation_exception_handler(request: Request, exc: RequestValidationError):
    return JSONResponse(
        status_code=422,
        content=format_validation_error_response(exc.errors())
    )

# Include routers
app.include_router(user_router)

# CORS middleware configuration
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # In production, replace with specific origins
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
async def root():
    return {"message": "Welcome to Expense Tracker API"}

@app.get("/health")
async def health_check(db: Session = Depends(get_db)):
    """Check if the database connection is working"""
    try:
        # Try to execute a simple query
        db.execute("SELECT 1")
        return {
            "status": "healthy",
            "database": "connected"
        }
    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=f"Database connection failed: {str(e)}"
        )

if __name__ == "__main__":
    uvicorn.run(
        "server:app",
        host="127.0.0.1",  # Remove http:// from host
        port=8000,
        reload=True,
        log_level="debug"
    )