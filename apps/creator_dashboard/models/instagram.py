from datetime import datetime

from pydantic import BaseModel, ConfigDict


class MediaResponse(BaseModel):
    
    model_config = ConfigDict(from_attributes=True)

    id: int

    caption: str | None

    thumbnail_url: str | None

    media_url: str | None

    permalink: str | None

    comments_count: int

    published_at: datetime | None


class CommentResponse(BaseModel):
    
    model_config = ConfigDict(from_attributes=True)

    id: int

    text: str | None

    author: str | None

    like_count: int

    published_at: datetime | None