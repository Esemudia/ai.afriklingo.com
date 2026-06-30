from TTS.api import TTS

from app.services.tts.base import BaseTTSModel


class CoquiTTSModel(BaseTTSModel):

    def __init__(self, model_name):

        print(f"Loading {model_name}")

        self.model = TTS(
            model_name=model_name,
            progress_bar=False
        )

    def speak(self, text, output_path):

        self.model.tts_to_file(
            text=text,
            file_path=output_path
        )