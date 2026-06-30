from fastapi import APIRouter

from app.models.schemas import TextRequest
from app.services.tts_service import TTSService

router = APIRouter(
    prefix="/tts",
    tags=["Text To Speech"]
)

tts = TTSService()


@router.post("/")
async def generate(request: TextRequest):

   return tts.generate(
        request.language,
        request.course,
        request.module,
        request.lesson,
        request.filename,
        request.text
    )