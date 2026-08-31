import os
import soundfile as sf
import librosa
import numpy as np

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

        try:
            y, sr = librosa.load(output, sr=None, mono=True)
            if y is not None and len(y) > 0:
                y_boost = y * 2.5  
                y_loud = np.tanh(y_boost) * 0.98  
                sf.write(output, y_loud, int(sr))
        except Exception as e:
            print(f"Error processing audio: {e}")

        return {

            "success":True,

            "audio":output

        }