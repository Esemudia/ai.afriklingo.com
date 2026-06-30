from fastapi import APIRouter
from app.services.stt_service import STTService

router = APIRouter(
    prefix="/stt",
    tags=["Speech To Text"]
)

service = STTService()


@router.post("/")
async def transcribe():

    return service.transcribe(None)