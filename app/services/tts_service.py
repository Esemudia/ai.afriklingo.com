import os

from app.services.model_manager import model_manager


class TTSService:

    def generate(
        self,
        language,
        course,
        module,
        lesson,
        filename,
        text
    ):

        folder = os.path.join(
            "audio",
            language,
            course,
            module,
            lesson
        )

        os.makedirs(folder, exist_ok=True)

        output = os.path.join(
            folder,
            filename + ".wav"
        )

        model = model_manager.get_tts(language)

        model.speak(
            text,
            output
        )

        return {

            "success":True,

            "audio":output

        }