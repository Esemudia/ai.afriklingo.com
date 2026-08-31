from faster_whisper import WhisperModel


class STTService:

    def __init__(self):

        self.model = None

    def load_model(self):

        if self.model is None:

            print("Loading Whisper model...")

            self.model = WhisperModel(
                "large-v3",
                device="cpu",
                compute_type="int8",
                local_files_only=True
            )

            print("Whisper model loaded successfully.")

    def transcribe(self, audio_path, language=None):

        self.load_model()
        assert self.model is not None, "Model failed to load"
        segments, info = self.model.transcribe(audio_path, language=language)

        transcript = ""

        for segment in segments:

            transcript += segment.text + " "

        return transcript.strip()