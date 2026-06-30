from fastapi import FastAPI

app = FastAPI(
    title="AfrikLingo AI",
    version="1.0.0"
)


@app.get("/")
async def root():
    return {
        "status": "running",
        "message": "AfrikLingo AI is ready 🚀"
    }