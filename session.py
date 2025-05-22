from livekit.agents import (
    AgentSession,
)
from livekit.plugins import (
    openai,
    silero,
    elevenlabs,
)
from livekit.plugins import deepgram, openai, silero
from livekit.plugins.turn_detector.multilingual import MultilingualModel

ELEVEN_LABS_CLAIRE = '6vTyAgAT8PncODBcLjRf'


def get_default_session() -> AgentSession:
    stt = openai.STT(
        language="fr",
        model="gpt-4o-mini-transcribe",
    )

    session = AgentSession(
        min_interruption_duration=3,
        vad=silero.VAD.load(),
        stt=stt,
        llm=openai.LLM(model="gpt-4o"),
        tts=elevenlabs.TTS(
            voice_id=ELEVEN_LABS_CLAIRE,
            model="eleven_multilingual_v2",
            voice_settings=elevenlabs.VoiceSettings(stability=1, speed=1.11, similarity_boost=1)
        ),
        min_endpointing_delay=1,
        turn_detection=MultilingualModel(),
    )
    return session