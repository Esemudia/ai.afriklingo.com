LANGUAGE_MODELS = {

    # ======================================
    # ENGLISH
    # ======================================
    "en": {
        "name": "English",
        "provider": "coqui",
        "tts_model": "tts_models/en/ljspeech/tacotron2-DDC",
        "stt_model": "openai/whisper-large-v3",
        "translation_model": "facebook/nllb-200-distilled-600M"
    },

    # ======================================
    # SWAHILI
    # ======================================
    "sw": {
        "name": "Swahili",
        "provider": "huggingface",
        "tts_model": "facebook/mms-tts-swh",
        "stt_model": "openai/whisper-large-v3",
        "translation_model": "facebook/nllb-200-distilled-600M"
    },

    # ======================================
    # YORUBA
    # ======================================
    "yo": {
        "name": "Yoruba",
        "provider": "azure",
        "tts_model": "yo-NG-Neural",
        "stt_model": "openai/whisper-large-v3",
        "translation_model": "facebook/nllb-200-distilled-600M"
    },

    # ======================================
    # HAUSA
    # ======================================
    "ha": {
        "name": "Hausa",
        "provider": "azure",
        "tts_model": "ha-NG-Neural",
        "stt_model": "openai/whisper-large-v3",
        "translation_model": "facebook/nllb-200-distilled-600M"
    },

    # ======================================
    # AMHARIC
    # ======================================
    "am": {
        "name": "Amharic",
        "provider": "azure",
        "tts_model": "am-ET-Neural",
        "stt_model": "openai/whisper-large-v3",
        "translation_model": "facebook/nllb-200-distilled-600M"
    },

    # ======================================
    # ZULU
    # ======================================
    "zu": {
        "name": "Zulu",
        "provider": "azure",
        "tts_model": "zu-ZA-Neural",
        "stt_model": "openai/whisper-large-v3",
        "translation_model": "facebook/nllb-200-distilled-600M"
    },

    # ======================================
    # XHOSA
    # ======================================
    "xh": {
        "name": "Xhosa",
        "provider": "azure",
        "tts_model": "xh-ZA-Neural",
        "stt_model": "openai/whisper-large-v3",
        "translation_model": "facebook/nllb-200-distilled-600M"
    },

    # ======================================
    # SOMALI
    # ======================================
    "so": {
        "name": "Somali",
        "provider": "google",
        "tts_model": "so-SO-Standard-A",
        "stt_model": "openai/whisper-large-v3",
        "translation_model": "facebook/nllb-200-distilled-600M"
    },

    # ======================================
    # IGBO
    # ======================================
    "ig": {
        "name": "Igbo",
        "provider": "xtts",
        "tts_model": "afriklingo/igbo-xtts-v1",
        "stt_model": "openai/whisper-large-v3",
        "translation_model": "facebook/nllb-200-distilled-600M"
    },

    # ======================================
    # KINYARWANDA
    # ======================================
    "rw": {
        "name": "Kinyarwanda",
        "provider": "xtts",
        "tts_model": "afriklingo/kinyarwanda-xtts-v1",
        "stt_model": "openai/whisper-large-v3",
        "translation_model": "facebook/nllb-200-distilled-600M"
    },

    # ======================================
    # LUGANDA
    # ======================================
    "lg": {
        "name": "Luganda",
        "provider": "xtts",
        "tts_model": "afriklingo/luganda-xtts-v1",
        "stt_model": "openai/whisper-large-v3",
        "translation_model": "facebook/nllb-200-distilled-600M"
    },

    # ======================================
    # SHONA
    # ======================================
    "sn": {
        "name": "Shona",
        "provider": "xtts",
        "tts_model": "afriklingo/shona-xtts-v1",
        "stt_model": "openai/whisper-large-v3",
        "translation_model": "facebook/nllb-200-distilled-600M"
    },

    # ======================================
    # TWI
    # ======================================
    "tw": {
        "name": "Twi",
        "provider": "xtts",
        "tts_model": "afriklingo/twi-xtts-v1",
        "stt_model": "openai/whisper-large-v3",
        "translation_model": "facebook/nllb-200-distilled-600M"
    },

    # ======================================
    # EWE
    # ======================================
    "ee": {
        "name": "Ewe",
        "provider": "xtts",
        "tts_model": "afriklingo/ewe-xtts-v1",
        "stt_model": "openai/whisper-large-v3",
        "translation_model": "facebook/nllb-200-distilled-600M"
    },

    # ======================================
    # WOLOF
    # ======================================
    "wo": {
        "name": "Wolof",
        "provider": "xtts",
        "tts_model": "afriklingo/wolof-xtts-v1",
        "stt_model": "openai/whisper-large-v3",
        "translation_model": "facebook/nllb-200-distilled-600M"
    },

    # ======================================
    # LINGALA
    # ======================================
    "ln": {
        "name": "Lingala",
        "provider": "xtts",
        "tts_model": "afriklingo/lingala-xtts-v1",
        "stt_model": "openai/whisper-large-v3",
        "translation_model": "facebook/nllb-200-distilled-600M"
    }
}