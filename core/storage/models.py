from datetime import datetime
from enum import Enum
from sqlalchemy import Boolean, ForeignKey, Integer, String, Text
from sqlalchemy import Enum as SqlEnum
from sqlalchemy.orm import relationship, mapped_column, Mapped

from .database import Base

class Platform(str, Enum):
    INSTAGRAM = "instagram"
    YOUTUBE = "youtube"

class ReplyStatus(str, Enum):
    DRAFT = "draft"
    APPROVED = "approved"
    POSTED = "posted"
    
class SocialAccount(Base):
    __tablename__ = "social_accounts"

    platform: Mapped[Platform] = mapped_column(SqlEnum(Platform))
    
    username: Mapped[str] = mapped_column(String(100))

    display_name: Mapped[str | None]

    platform_user_id: Mapped[str] = mapped_column(
        String(128),
        unique=True,
    )

    access_token: Mapped[str | None]
    
    refresh_token: Mapped[str | None]

    media = relationship(
        "Media",
        back_populates="account",
    )

class Media(Base):
    __tablename__ = "media"

    account_id: Mapped[int] = mapped_column(
        ForeignKey("social_accounts.id")
    )

    platform_media_id: Mapped[str] = mapped_column(
        String(128),
        unique=True,
    )
    
    title: Mapped[str | None]

    caption: Mapped[str | None] = mapped_column(Text)

    thumbnail_url: Mapped[str | None]

    media_url: Mapped[str | None]

    permalink: Mapped[str | None]

    published_at: Mapped[datetime | None]

    account = relationship(
        "SocialAccount",
        back_populates="media",
    )

    comments = relationship(
        "Comment",
        back_populates="media",
        cascade="all, delete-orphan",
    )

    comments_count: Mapped[int] = mapped_column(
        Integer,
        default=0,
    )


class Comment(Base):
    __tablename__ = "comments"

    media_id: Mapped[int] = mapped_column(
        ForeignKey("media.id")
    )

    platform_comment_id: Mapped[str] = mapped_column(
        String(128),
        unique=True,
    )

    author: Mapped[str | None] = mapped_column(
        String(255),
        nullable=True,
    )

    text: Mapped[str | None] = mapped_column(
        Text,
        nullable=True,
    )

    like_count: Mapped[int] = mapped_column(
        Integer,
        default=0,
    )

    is_hidden: Mapped[bool] = mapped_column(
        Boolean,
        default=False,
    )

    is_replied: Mapped[bool] = mapped_column(
        Boolean,
        default=False,
    )

    published_at: Mapped[datetime | None]

    media = relationship(
        "Media",
        back_populates="comments",
    )

    replies = relationship(
        "Reply",
        back_populates="comment",
        cascade="all, delete-orphan",
    )

class Reply(Base):
    __tablename__ = "replies"

    comment_id: Mapped[int] = mapped_column(
        ForeignKey("comments.id")
    )

    draft: Mapped[str] = mapped_column(Text)

    edited: Mapped[str | None] = mapped_column(Text)

    posted: Mapped[str | None] = mapped_column(Text)

    status: Mapped[ReplyStatus] = mapped_column(
        SqlEnum(ReplyStatus),
        default=ReplyStatus.DRAFT,
    )

    comment = relationship(
        "Comment",
        back_populates="replies",
    )

