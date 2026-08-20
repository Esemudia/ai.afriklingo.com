from TTS.api import TTS

from app.services.tts.base import BaseTTSModel


class CoquiTTSModel(BaseTTSModel):

    def __init__(self, model):

        self.tts = TTS(model)

    def speak(
        self,
        text,
        output_path
    ):

        self.tts.tts_to_file(
            text=text,
            file_path=output_path
        )