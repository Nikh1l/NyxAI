from core.social.instagram.client import InstagramClient
from core.social.instagram.repository import InstagramRepository
from core.storage.database import SessionLocal


class InstagramService:

    def list_media(self):
        with SessionLocal() as session:
            repo = InstagramRepository(session)
            return repo.list_media()
        
    def get_media(self, media_id: int):
        with SessionLocal() as session:
            repo = InstagramRepository(session)
            return repo.get_media(media_id)
        
    def list_comments(self, media_id: int):
        with SessionLocal() as session:
            repo = InstagramRepository(session)
            return repo.list_comments(media_id)