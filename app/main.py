from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(
    title="FastAPI Backend",
    description="FastAPI + PostgreSQL + SQLAlchemy Project",
    version="1.0.0"
)

# CORS Configuration
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Home Route
@app.get("/")
async def root():
    return {
        "message": "Welcome to FastAPI Backend",
        "status": "running"
    }

# Health Check Route
@app.get("/health")
async def health_check():
    return {
        "success": True,
        "message": "Server is healthy"
    }

# Example API Route
@app.get("/api/v1")
async def api_version():
    return {
        "version": "v1",
        "framework": "FastAPI"
    }

