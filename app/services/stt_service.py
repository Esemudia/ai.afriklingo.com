from faster_whisper import WhisperModel


class STTService:

    def __init__(self):

        self.model = None

    def load_model(self):

        if self.model is None:

            print("Loading Whisper model...")

            self.model = WhisperModel(
                "small",
                device="cpu",
                compute_type="int8"
            )

            print("Whisper model loaded successfully.")

    def transcribe(self, audio_path):

        self.load_model()
        assert self.model is not None, "Model failed to load"
        segments, info = self.model.transcribe(audio_path)

        transcript = ""

        for segment in segments:

            transcript += segment.text + " "

        return transcript.strip()