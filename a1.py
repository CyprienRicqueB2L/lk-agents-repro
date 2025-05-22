
from collections.abc import Coroutine
import logging
from session import get_default_session
from dotenv import load_dotenv
from livekit.agents import (
    Agent,
    JobContext,
    WorkerOptions,
    cli,
)
from livekit.agents.voice.agent import ModelSettings


logger = logging.getLogger("a1")

load_dotenv()


class BAgent(Agent):
    def __init__(self, job_context: JobContext) -> None:
        self.job_context = job_context
        self.i = 0

        super().__init__(
            instructions="Aide l'autre agent"
        )
        logger.info("Agent initialized")

    async def on_enter(self):
        logger.info("Agent entered room")
        self.session.say("Bonjour, comment vas-tu? Je suis la pour t'aider avec toutes tes questions.")

    async def stt_node(self, audio, model_settings: ModelSettings):
        print("[stt_node] Received audio stream")
        return super().stt_node(audio, model_settings)


async def entrypoint(ctx: JobContext):
    session = get_default_session()

    await ctx.connect()

    await session.start(
        agent=BAgent(job_context=ctx),
        room=ctx.room
    )


if __name__ == "__main__":
    cli.run_app(WorkerOptions(entrypoint_fnc=entrypoint, agent_name="a1"))
