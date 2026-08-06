from app.services.tts.base import BaseTTSModel


class XTTSModel(BaseTTSModel):

    def __init__(self, model_name):

        self.model_name = model_name

    def speak(self, text, output_path):

        raise NotImplementedError(
            "Custom XTTS model not implemented yet."
        )