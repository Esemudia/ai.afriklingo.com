import azure.cognitiveservices.speech as speechsdk
import os


class AzureTTSModel:

    def __init__(self, voice):

        self.voice = voice

        self.key = os.getenv("AZURE_SPEECH_KEY")
        self.region = os.getenv("AZURE_SPEECH_REGION")

        if not self.key or not self.region:
            raise Exception(
                "Azure Speech credentials are missing."
            )

    def speak(self, text, output):

        config = speechsdk.SpeechConfig(
            subscription=self.key,
            region=self.region
        )

        config.speech_synthesis_voice_name = self.voice

        audio = speechsdk.audio.AudioOutputConfig(
            filename=output
        )

        synthesizer = speechsdk.SpeechSynthesizer(
            speech_config=config,
            audio_config=audio
        )

        result = synthesizer.speak_text_async(text).get()

        if result is None or result.reason != speechsdk.ResultReason.SynthesizingAudioCompleted:
            raise Exception("Azure synthesis failed.")