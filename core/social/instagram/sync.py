from core.social.instagram.client import InstagramClient
from core.storage.database import SessionLocal
from core.storage.models import Platform, SocialAccount, Media, Comment
from datetime import datetime

class InstagramSyncService:

    def __init__(self, access_token: str):
        self.client = InstagramClient(access_token)
        
    async def sync(self):
        profile = await self.client.me()
        media_items = await self.client.media()

        with SessionLocal() as session:
            account = self._upsert_account(session, profile)
            media_lookup = self._upsert_media(
                session,
                account.id,
                media_items,
            )

            for item in media_items:
                comments = await self.client.comments(item["id"])
                print(f"Media: {item['id']} - Comments: {len(comments)}")

                self._upsert_comments(
                    session,
                    media_lookup[item["id"]].id,
                    comments,
                )

            session.commit()

    def _upsert_account(self, session, profile) -> SocialAccount:
        account = (
            session.query(SocialAccount)
            .filter_by(
                platform=Platform.INSTAGRAM,
                platform_user_id=profile["id"],
            )
            .first()
        )

        if account:
            account.username = profile["username"]
            account.display_name = profile.get("name")
            return account
        
        account = SocialAccount(
            platform=Platform.INSTAGRAM,
            platform_user_id=profile["id"],
            username=profile["username"],
            display_name=profile.get("name"),
        )

        session.add(account)
        session.flush()

        return account
    

    def _upsert_media(self, session, account_id: int, media_list: list):
        
        media_lookup = {}
        
        for item in media_list:
            media = (
                session.query(Media)
                .filter_by(platform_media_id=item["id"])
                .first()
            )    

            if media:
                media.caption = item.get("caption")
                media.media_url = item.get("media_url")
                media.thumbnail_url = item.get("thumbnail_url")
                media.permalink = item.get("permalink")
                media.comments_count = item.get("comments_count", 0)
                
                if item.get("timestamp"):
                    media.published_at = datetime.fromisoformat(
                        item["timestamp"].replace("Z", "+00:00")
                    )

                continue

            else:
                media = Media(
                    account_id=account_id,
                    platform_media_id=item["id"],
                    caption=item.get("caption"),
                    media_url=item.get("media_url"),
                    thumbnail_url=item.get("thumbnail_url"),
                    permalink=item.get("permalink"),
                    comments_count=item.get("comments_count", 0),
                    published_at=(
                        datetime.fromisoformat(
                            item["timestamp"].replace("Z", "+00:00")
                        )
                        if item.get("timestamp")
                        else None
                    ),
                )

                session.add(media)
                session.flush() 
            media_lookup[item["id"]] = media
        return media_lookup
    
        


    def _upsert_comments(self, session, media_id: int, comments: list):
        for item in comments:
            comment = (
                session.query(Comment)
                .filter_by(
                    platform_comment_id=item["id"]
                )
                .first()
            )

            if comment:
                comment.author = item.get("username")
                comment.text = item.get("text")
                comment.like_count = item.get("like_count", 0)
                continue

            comment = Comment(
                media_id=media_id,
                platform_comment_id=item["id"],
                author=item.get("username"),
                text=item.get("text"),
                like_count=item.get("like_count", 0),
                published_at=(
                    datetime.fromisoformat(
                        item["timestamp"].replace("Z", "+00:00")
                    )
                    if item.get("timestamp")
                    else None
                ),
            )
            session.add(comment)