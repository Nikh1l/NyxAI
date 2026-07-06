import asyncio
import os

from dotenv import load_dotenv

from core.social.instagram.service import InstagramService

load_dotenv

async def main():
    service = InstagramService(os.getenv("INSTAGRAM_ACCESS_TOKEN"))
    
    result = await service.post_reply(
        comment_id="18149183659497072",
        message="Thanks a lot! I appreciate it!",
    )

    print(result)

if __name__ == "__main__":
    asyncio.run(main())