from datetime import datetime

from sqlalchemy import DateTime
from sqlalchemy import create_engine
from sqlalchemy import func
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import sessionmaker

from core.config.settings import settings


class Base(DeclarativeBase):
    """Base for all database models."""

    id: Mapped[int] = mapped_column(
        primary_key=True,
        autoincrement=True,
    )

    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        server_default=func.now(),
    )

    updated_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        server_default=func.now(),
        onupdate=func.now(),
    )


engine = create_engine(
    settings.database_url,
    echo=True,
)

SessionLocal = sessionmaker(bind=engine)