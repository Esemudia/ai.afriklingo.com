from pydantic import BaseModel


class TextRequest(BaseModel):

    language: str

    course: str

    module: str

    lesson: str

    filename: str

    text: str


class PronunciationRequest(BaseModel):
    expected: str
    audioPath: str