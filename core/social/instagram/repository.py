from sqlalchemy.orm import Session
from core.storage.models import Media, Comment

class InstagramRepository:

    def __init__(self, session: Session):
        self.session = session


    def list_media(self) -> list[Media]:
        return (
            self.session.query(Media)
            .order_by(Media.published_at.desc())
            .all()
        )
    
    def get_media(self, media_id: str) -> Media | None:
        return (
            self.session.query(Media)
            .filter_by(id=media_id)
            .first()
        )
    
    def list_comments(self, media_id: int) -> list[Comment]:
        return (
            self.session.query(Comment)
            .filter_by(media_id=media_id)
            .order_by(Comment.published_at.desc())
            .all()
        )