from difflib import SequenceMatcher

from app.services.stt_service import STTService


class PronunciationService:

    def __init__(self):

        self.stt = STTService()

    def score(
        self,
        expected,
        audio_path
    ):

        transcript = self.stt.transcribe(
            audio_path
        )

        similarity = SequenceMatcher(
            None,
            expected.lower(),
            transcript.lower()
        ).ratio()

        score = round(
            similarity * 100,
            2
        )

        if score > 90:

            feedback = "Excellent"

        elif score > 75:

            feedback = "Good"

        elif score > 50:

            feedback = "Needs Improvement"

        else:

            feedback = "Try Again"

        return {

            "expected": expected,

            "transcript": transcript,

            "score": score,

            "feedback": feedback

        }