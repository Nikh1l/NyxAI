from core.social.instagram.client import InstagramClient
from core.storage.database import SessionLocal
from core.storage.models import Platform, SocialAccount, Media
from datetime import datetime

class InstagramSyncService:

    def __init__(self, access_token: str):
        self.client = InstagramClient(access_token)
        
    async def sync(self):
        profile = await self.client.me()
        media_items = await self.client.media()

        with SessionLocal() as session:
            account = self._upsert_account(session, profile)
            self._upsert_media(session, account.id, media_items)

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
                
                if item.get("timestamp"):
                    media.published_at = datetime.fromisoformat(
                        item["timestamp"].replace("Z", "+00:00")
                    )

                continue

            media = Media(
                account_id=account_id,
                platform_media_id=item["id"],
                caption=item.get("caption"),
                media_url=item.get("media_url"),
                thumbnail_url=item.get("thumbnail_url"),
                permalink=item.get("permalink"),
                published_at=(
                    datetime.fromisoformat(
                        item["timestamp"].replace("Z", "+00:00")
                    )
                    if item.get("timestamp")
                    else None
                ),
            )

            session.add(media)