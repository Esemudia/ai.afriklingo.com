from app.config.languages import LANGUAGE_MODELS

from app.services.tts.coqui_model import CoquiTTSModel
from app.services.tts.huggingface_model import HuggingFaceTTSModel
from app.services.tts.azure_model import AzureTTSModel
from app.services.tts.google_model import GoogleTTSModel
from app.services.tts.xtts_model import XTTSModel


class ModelManager:

    def __init__(self):

        self.loaded_models = {}

    def _build_model(self, provider):

        engine = provider["engine"]

        model_name = provider["model"]

        if engine == "coqui":
            return CoquiTTSModel(model_name)

        if engine == "huggingface":
            return HuggingFaceTTSModel(model_name)

        if engine == "azure":
            return AzureTTSModel(model_name)

        if engine == "google":
            return GoogleTTSModel(model_name)

        if engine == "xtts":
            return XTTSModel(model_name)

        raise Exception(
            f"Unsupported engine: {engine}"
        )

    def get_tts(self, language):

        if language not in LANGUAGE_MODELS:
            raise Exception(
                f"Unsupported language: {language}"
            )

        if language in self.loaded_models:
            return self.loaded_models[language]

        config = LANGUAGE_MODELS[language]

        providers = config["providers"]

        last_error = None

        for provider in providers:

            try:

                model = self._build_model(provider)

                self.loaded_models[language] = model

                print(
                    f"{language} -> {provider['engine']} loaded."
                )

                return model

            except Exception as e:

                print(
                    f"{provider['engine']} failed:"
                )

                print(e)

                last_error = e

        raise Exception(
            f"No provider available for {language}: {last_error}"
        )


model_manager = ModelManager()