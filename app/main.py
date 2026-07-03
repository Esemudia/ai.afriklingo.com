
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.routers import tts, stt, pronunciation

app = FastAPI(
    title="AfrikLingo AI",
    version="1.0.0"
)

# Allow CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(tts.router)
app.include_router(stt.router)
app.include_router(pronunciation.router)


@app.get("/")
async def root():
    return {
        "status": "running",
        "message": "AfrikLingo AI is ready 🚀"
    }
