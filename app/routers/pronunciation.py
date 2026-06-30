from fastapi import APIRouter
from app.models.schemas import PronunciationRequest
from app.services.pronunciation_service import PronunciationService

router = APIRouter(
    prefix="/pronunciation",
    tags=["Pronunciation"]
)

service = PronunciationService()


@router.post("/")
async def pronunciation(data: PronunciationRequest):

    return service.score(data.expected)