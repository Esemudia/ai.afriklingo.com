from fastapi import FastAPI
from app.routers import tts, stt, pronunciation

app = FastAPI(
    title="AfrikLingo AI",
    version="1.0.0"
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