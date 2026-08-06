from app.services.tts.base import BaseTTSModel


class GoogleTTSModel(BaseTTSModel):

    def __init__(self, voice):

        self.voice = voice

    def speak(self, text, output_path):

        raise NotImplementedError(
            "Google Cloud TTS integration not implemented yet."
        )