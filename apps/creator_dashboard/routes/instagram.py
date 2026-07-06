from fastapi import APIRouter
from apps.creator_dashboard.models.instagram import MediaResponse, CommentResponse

from core.social.instagram.service import InstagramService

router = APIRouter(
    prefix="/instagram",
    tags=["Instagram"],
)

service = InstagramService()

@router.get(
    "/media",
    response_model=list[MediaResponse]
)
async def list_media():
    return service.list_media()

@router.get(
    "/media/{media_id}/comments",
    response_model=list[CommentResponse]
)
async def get_comments(media_id: int):
    return service.list_comments(media_id)