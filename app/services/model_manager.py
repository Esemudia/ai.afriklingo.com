from app.config.languages import LANGUAGE_MODELS

from app.services.tts.coqui_model import CoquiTTSModel
from app.services.tts.huggingface_model import HuggingFaceTTSModel
from app.services.tts.azure_model import AzureTTSModel
from app.services.tts.google_model import GoogleTTSModel
from app.services.tts.xtts_model import XTTSModel


class ModelManager:

    def __init__(self):
        self.loaded_models = {}

    def get_tts(self, language):

        if language not in LANGUAGE_MODELS:
            raise Exception(f"Unsupported language: {language}")

        if language in self.loaded_models:
            return self.loaded_models[language]

        config = LANGUAGE_MODELS[language]

        provider = config["provider"]

        if provider == "coqui":

            model = CoquiTTSModel(
                config["tts_model"]
            )

        elif provider == "huggingface":

            model = HuggingFaceTTSModel(
                config["tts_model"]
            )

        elif provider == "azure":

            model = AzureTTSModel(
                voice=config["tts_model"]
            )

        elif provider == "google":

            model = GoogleTTSModel(
                voice=config["tts_model"]
            )

        elif provider == "xtts":

            model = XTTSModel(
                config["tts_model"]
            )

        else:

            raise Exception(
                f"Unsupported provider: {provider}"
            )

        self.loaded_models[language] = model

        return model


model_manager = ModelManager()