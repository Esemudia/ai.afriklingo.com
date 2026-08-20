from fastapi import APIRouter, UploadFile, File
from app.services.stt_service import STTService

import os

router = APIRouter(

    prefix="/stt",

    tags=["Speech To Text"]

)

service = STTService()


@router.post("/")

async def transcribe(

    audio: UploadFile = File(...)

):

    path = "temp.wav"

    with open(path, "wb") as f:

        f.write(await audio.read())

    text = service.transcribe(path)

    os.remove(path)

    return {

        "text": text

    }