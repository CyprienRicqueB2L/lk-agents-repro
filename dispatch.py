import asyncio
import logging
from uuid import uuid4
from dotenv import load_dotenv
from livekit import api
from livekit.api import DeleteRoomRequest

logger = logging.getLogger("room-manager")
logger.setLevel(logging.INFO)

load_dotenv()

async def send_agent_to_room(room_name: str, agent_name: str, lk_api: api.LiveKitAPI):
    print(f"Sending agent {agent_name} to room {room_name}")
    await lk_api.agent_dispatch.create_dispatch(
        api.CreateAgentDispatchRequest(
            agent_name=agent_name,
            room=room_name
        )
    )

async def create_and_dispatch():
    room_name = f"test_room_{uuid4().hex[:8]}"
    
    lk_api = api.LiveKitAPI()
    
    await asyncio.sleep(7)
    try:
        await send_agent_to_room(room_name, "a1", lk_api)
        await send_agent_to_room(room_name, "a2", lk_api)
        logger.info("Agent dispatched successfully")
        
        return room_name

    except Exception as e:
        logger.error(f"Error in room creation/dispatch: {e}", exc_info=True)
        raise
    finally:
        await lk_api.aclose()


async def cleanup_room(room_name: str):
    logger.info(f"Cleaning up room: {room_name}")
    lk_api = api.LiveKitAPI()
    try:
        await lk_api.room.delete_room(DeleteRoomRequest(room=room_name))
        logger.info(f"Room deleted: {room_name}")
    except Exception as e:
        logger.error(f"Error cleaning up room: {e}", exc_info=True)
    finally:
        await lk_api.aclose()


async def main():
    room_name = None
    # try:
    room_name = await create_and_dispatch()
        # input("Press Enter to cleanup the room...")
    # finally:
    #     await cleanup_room(room_name)


if __name__ == "__main__":
    asyncio.run(main()) 