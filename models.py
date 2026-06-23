from xml.dom.minidom import Comment

from sqlalchemy import Integer, String, ForeignKey, DateTime, func
from sqlalchemy.orm import Mapped, mapped_column, relationship
from database.orm import Base
from datetime import datetime


# Article 모델 정의
class Article(Base):
    __tablename__ = 'article' # 테이블 이름

    id : Mapped[int] = mapped_column(Integer, primary_key=True,autoincrement=True)

    title : Mapped[String] = mapped_column(String(255))

    content : Mapped[String] = mapped_column(String(1000))

    comments: Mapped[list["Comment"]] = relationship(back_populates="article", cascade="all, delete-orphan")

#Comment 모델
class Comments(Base):
    __tablename__ = 'comment'

    id : Mapped[int] = mapped_column(Integer, primary_key=True,autoincrement=True)
    author: Mapped[String] = mapped_column(String(20))
    content: Mapped[String] = mapped_column(String(200))
    created_at : Mapped[datetime] = mapped_column(DateTime, server_default=func.now())
    article_id : Mapped[Article] = mapped_column(ForeignKey("article.id"), nullable=False)
    article: Mapped[Article] = relationship(back_populates="comments")