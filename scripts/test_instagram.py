import asyncio
import os

from dotenv import load_dotenv
from core.social.instagram.sync import InstagramSyncService
load_dotenv()

async def main():
    token = os.environ["INSTAGRAM_ACCESS_TOKEN"]
    service = InstagramSyncService(token)
    await service.sync()

asyncio.run(main())