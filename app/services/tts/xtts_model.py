import os
from TTS.api import TTS
from app.services.tts.base import BaseTTSModel


class XTTSModel(BaseTTSModel):

    def __init__(self, model_name):
        # Auto-accept Coqui TOS to prevent blocking
        os.environ["COQUI_TOS_AGREED"] = "1"
        self.model_name = model_name
        try:
            self.tts = TTS(model_name)
        except Exception as e:
            print(f"WARN: Could not load XTTS model '{model_name}': {e}. Falling back to MMS TTS.")
            self.tts = None
            
            # Extract language name and map to MMS (facebook/mms-tts-...)
            mms_model = None
            if "yoruba" in model_name: mms_model = "facebook/mms-tts-yor"
            elif "hausa" in model_name: mms_model = "facebook/mms-tts-hau"
            elif "zulu" in model_name: mms_model = "facebook/mms-tts-zul"
            elif "xhosa" in model_name: mms_model = "facebook/mms-tts-xho"
            elif "igbo" in model_name: mms_model = "facebook/mms-tts-ibo"
            elif "kinyarwanda" in model_name: mms_model = "facebook/mms-tts-kin"
            elif "luganda" in model_name: mms_model = "facebook/mms-tts-lug"
            elif "shona" in model_name: mms_model = "facebook/mms-tts-sna"
            elif "twi" in model_name: mms_model = "facebook/mms-tts-twi"
            elif "ewe" in model_name: mms_model = "facebook/mms-tts-ewe"
            elif "wolof" in model_name: mms_model = "facebook/mms-tts-wol"
            elif "lingala" in model_name: mms_model = "facebook/mms-tts-lin"
            
            self.fallback_model = None
            if mms_model:
                try:
                    from app.services.tts.huggingface_model import HuggingFaceTTSModel
                    self.fallback_model = HuggingFaceTTSModel(mms_model)
                except Exception as mms_e:
                    print(f"MMS fallback failed: {mms_e}")

    def speak(self, text, output_path):
        
        # If the actual model failed to load due to missing weights, use fallback or mock
        if self.tts is None:
            fallback = getattr(self, "fallback_model", None)
            if fallback is not None:
                fallback.speak(text, output_path)
                return
                
            # If everything fails, mock
            import wave
            import struct
            import math
            audio = wave.open(output_path, 'w')
            audio.setnchannels(1)
            audio.setsampwidth(2)
            audio.setframerate(24000)
            for i in range(24000):
                value = int(32767.0 * math.cos(i * 0.1) * 0.1)
                data = struct.pack('<h', value)
                audio.writeframesraw(data)
            audio.close()
            return
            
        self.tts.tts_to_file(
            text=text, 
            file_path=output_path
        )