from sqlalchemy import Integer, String, Boolean
from sqlalchemy.orm import Mapped, mapped_column
from database.orm import Base

# Article 모델 정의
class Article(Base):
    __tablename__ = 'article' # 테이블 이름

    id : Mapped[int] = mapped_column(Integer, primary_key=True,autoincrement=True)

    title : Mapped[String] = mapped_column(String(255))

    content : Mapped[String] = mapped_column(String(1000))

