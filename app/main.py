from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.middleware.cors import CORSMiddleware
from .routers import contact
from .database import engine, Base
import os

# Create database tables
Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="Sanaullah Farooq Portfolio API",
    description="Backend for portfolio website",
    version="1.0.0"
)

# CORS Middleware
origins = [
    "http://localhost",
    "http://localhost:8000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Mount static files
static_dir = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "static")
if not os.path.exists(static_dir):
    os.makedirs(static_dir)

app.mount("/static", StaticFiles(directory=static_dir), name="static")

# Include routers
app.include_router(contact.router, prefix="/api", tags=["Contact"])

@app.get("/health")
def health_check():
    return {"status": "ok"}

# Serve index.html for root - simplistic way for SPA
from fastapi.responses import FileResponse

@app.get("/")
async def read_index():
    return FileResponse(os.path.join(static_dir, 'index.html'))
