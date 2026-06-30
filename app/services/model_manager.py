from app.config.languages import LANGUAGE_MODELS

from app.services.tts.coqui_model import CoquiTTSModel

from app.services.tts.huggingface_model import HuggingFaceTTSModel


class ModelManager:

    def __init__(self):

        self.loaded_models = {}

    def get_tts(self, language):

        if language not in LANGUAGE_MODELS:

            raise Exception(
                "Unsupported language"
            )

        if language in self.loaded_models:

            return self.loaded_models[language]

        config = LANGUAGE_MODELS[language]

        if config["engine"] == "coqui":

            model = CoquiTTSModel(
                config["model"]
            )

        elif config["engine"] == "huggingface":

            model = HuggingFaceTTSModel(
                config["model"]
            )

        else:

            raise Exception(
                "Unknown engine"
            )

        self.loaded_models[language] = model

        return model


model_manager = ModelManager()