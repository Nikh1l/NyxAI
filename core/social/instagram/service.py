from core.social.instagram.client import InstagramClient
from core.storage.database import SessionLocal
from core.storage.models import Comment, Reply, ReplyStatus 

class InstagramService:

    def __init__(self, access_token: str):
        self.client = InstagramClient(access_token)

    async def post_reply(self, comment_id: str, message: str,):
        result = await self.client.reply(
            comment_id=comment_id,
            message=message,
        )

        with SessionLocal() as session:
            comment = (
                session.query(Comment)
                .filter_by(
                    platform_comment_id=comment_id
                )
                .first()
            )

            reply = Reply(
                comment_id=comment.id,
                draft=message,
                posted=message,
                status=ReplyStatus.POSTED
            )

            session.add(reply)
            session.commit()
        return result
