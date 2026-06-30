import torch
import scipy.io.wavfile

from transformers import (
    AutoTokenizer,
    VitsModel
)

from app.services.tts.base import BaseTTSModel


class HuggingFaceTTSModel(BaseTTSModel):

    def __init__(self, model_name):

        print(f"Loading {model_name}")

        self.tokenizer = AutoTokenizer.from_pretrained(
            model_name
        )

        self.model = VitsModel.from_pretrained(
            model_name
        )

    def speak(self, text, output_path):

        inputs = self.tokenizer(
            text,
            return_tensors="pt"
        )

        with torch.no_grad():

            waveform = self.model(
                **inputs
            ).waveform

        scipy.io.wavfile.write(
            output_path,
            rate=self.model.config.sampling_rate,
            data=waveform.squeeze().cpu().numpy()
        )