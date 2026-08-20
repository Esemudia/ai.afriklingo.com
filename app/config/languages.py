LANGUAGE_MODELS = {

    # ======================================
    # ENGLISH
    # ======================================
    "en": {
        "name": "English",
        "providers": [
            {
                "engine": "coqui",
                "model": "tts_models/en/ljspeech/tacotron2-DDC"
            }
        ],
        "stt_model": "large-v3",
        "translation_model": "facebook/nllb-200-distilled-600M"
    },

    # ======================================
    # SWAHILI
    # ======================================
    "sw": {
        "name": "Swahili",
        "providers": [
            {
                "engine": "huggingface",
                "model": "facebook/mms-tts-swh"
            }
        ],
        "stt_model": "large-v3",
        "translation_model": "facebook/nllb-200-distilled-600M"
    },

    # ======================================
    # AMHARIC
    # ======================================
    "am": {
        "name": "Amharic",
        "providers": [
            {
                "engine": "huggingface",
                "model": "facebook/mms-tts-amh"
            }
        ],
        "stt_model": "large-v3",
        "translation_model": "facebook/nllb-200-distilled-600M"
    },

    # ======================================
    # YORUBA
    # ======================================
    "yo": {
        "name": "Yoruba",
        "providers": [
            {
                "engine": "azure",
                "model": "yo-NG-Neural"
            },
            {
                "engine": "xtts",
                "model": "afriklingo/yoruba-xtts-v1"
            }
        ],
        "stt_model": "large-v3",
        "translation_model": "facebook/nllb-200-distilled-600M"
    },

    # ======================================
    # HAUSA
    # ======================================
    "ha": {
        "name": "Hausa",
        "providers": [
            {
                "engine": "azure",
                "model": "ha-NG-Neural"
            },
            {
                "engine": "xtts",
                "model": "afriklingo/hausa-xtts-v1"
            }
        ],
        "stt_model": "large-v3",
        "translation_model": "facebook/nllb-200-distilled-600M"
    },

    # ======================================
    # ZULU
    # ======================================
    "zu": {
        "name": "Zulu",
        "providers": [
            {
                "engine": "azure",
                "model": "zu-ZA-Neural"
            },
            {
                "engine": "xtts",
                "model": "afriklingo/zulu-xtts-v1"
            }
        ],
        "stt_model": "large-v3",
        "translation_model": "facebook/nllb-200-distilled-600M"
    },

    # ======================================
    # XHOSA
    # ======================================
    "xh": {
        "name": "Xhosa",
        "providers": [
            {
                "engine": "azure",
                "model": "xh-ZA-Neural"
            },
            {
                "engine": "xtts",
                "model": "afriklingo/xhosa-xtts-v1"
            }
        ],
        "stt_model": "large-v3",
        "translation_model": "facebook/nllb-200-distilled-600M"
    },

    # ======================================
    # IGBO
    # ======================================
    "ig": {
        "name": "Igbo",
        "providers": [
            {
                "engine": "xtts",
                "model": "afriklingo/igbo-xtts-v1"
            }
        ],
        "stt_model": "large-v3",
        "translation_model": "facebook/nllb-200-distilled-600M"
    },

    # ======================================
    # SOMALI
    # ======================================
    "so": {
        "name": "Somali",
        "providers": [
            {
                "engine": "google",
                "model": "so-SO-Standard-A"
            }
        ],
        "stt_model": "large-v3",
        "translation_model": "facebook/nllb-200-distilled-600M"
    },

    # ======================================
    # KINYARWANDA
    # ======================================
    "rw": {
        "name": "Kinyarwanda",
        "providers": [
            {
                "engine": "xtts",
                "model": "afriklingo/kinyarwanda-xtts-v1"
            }
        ],
        "stt_model": "large-v3",
        "translation_model": "facebook/nllb-200-distilled-600M"
    },

    # ======================================
    # LUGANDA
    # ======================================
    "lg": {
        "name": "Luganda",
        "providers": [
            {
                "engine": "xtts",
                "model": "afriklingo/luganda-xtts-v1"
            }
        ],
        "stt_model": "large-v3",
        "translation_model": "facebook/nllb-200-distilled-600M"
    },

    # ======================================
    # SHONA
    # ======================================
    "sn": {
        "name": "Shona",
        "providers": [
            {
                "engine": "xtts",
                "model": "afriklingo/shona-xtts-v1"
            }
        ],
        "stt_model": "large-v3",
        "translation_model": "facebook/nllb-200-distilled-600M"
    },

    # ======================================
    # TWI
    # ======================================
    "tw": {
        "name": "Twi",
        "providers": [
            {
                "engine": "xtts",
                "model": "afriklingo/twi-xtts-v1"
            }
        ],
        "stt_model": "large-v3",
        "translation_model": "facebook/nllb-200-distilled-600M"
    },

    # ======================================
    # EWE
    # ======================================
    "ee": {
        "name": "Ewe",
        "providers": [
            {
                "engine": "xtts",
                "model": "afriklingo/ewe-xtts-v1"
            }
        ],
        "stt_model": "large-v3",
        "translation_model": "facebook/nllb-200-distilled-600M"
    },

    # ======================================
    # WOLOF
    # ======================================
    "wo": {
        "name": "Wolof",
        "providers": [
            {
                "engine": "xtts",
                "model": "afriklingo/wolof-xtts-v1"
            }
        ],
        "stt_model": "large-v3",
        "translation_model": "facebook/nllb-200-distilled-600M"
    },

    # ======================================
    # LINGALA
    # ======================================
    "ln": {
        "name": "Lingala",
        "providers": [
            {
                "engine": "xtts",
                "model": "afriklingo/lingala-xtts-v1"
            }
        ],
        "stt_model": "large-v3",
        "translation_model": "facebook/nllb-200-distilled-600M"
    }

}