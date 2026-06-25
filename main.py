from sqlalchemy.ext.asyncio import session
from scheme.request import ArticleRequest, ArticleUpdateRequest, CommentRequest
from scheme.response import ArticleRequest, CommentResponse
from fastapi import FastAPI, status, HTTPException, Request
from models import Article, Comment
from sqlalchemy import select
from database.db_connection import engine, SessionFactory
from database.orm import Base
from starlette.middleware.sessions import SessionMiddleware
from scheme.request import LoginRequest

app = FastAPI()

Base.metadata.create_all(bind=engine)
# 세션 미들웨어 등록
app.add_middleware(SessionMiddleware, secret_key="your_secret_key")


# # 게시글 저장
# articles = [
#     {"id": 1, "title": "공부하기", "content": "fastapi 공부"},
#     {"id": 2, "title": "책 읽기", "content": "30페이지 읽기"},
#     {"id": 3, "title": "밥 먹기", "content": "저녁 먹기"}
# ]

# 로그인
@app.post("/login")
def login_handler(request: Request, body: LoginRequest):
    request.session["name"] = body.name
    return {"message": "Login Success"}

# 전체 게시글 조회
@app.get("/articles", response_model=ArticleRequest, status_code=status.HTTP_200_OK)
def get_articles():
    session = SessionFactory()
    try:
        stmt = select(Article)
        articles = session.execute(stmt).scalars().all()
        return articles
    finally:
        session.close()

# 단일 게시글 조회
@app.get("/articles/{article_id}", response_model=ArticleRequest, status_code=status.HTTP_200_OK)
def get_article(article_id: int):
    session = SessionFactory()
    try:
        stmt = select(Article).where(Article.id == article_id)
        article = session.execute(stmt).scalars().first()
        if article :
            return article
        raise HTTPException(status_code=404, detail="Article Not found.")
    finally:
        session.close()


# 게시글 생성
@app.post("/articles", response_model=ArticleRequest, status_code=status.HTTP_201_CREATED)
def create_article(body: ArticleRequest):
    session = SessionFactory()
    try:
        article = Article(title=body.title, content=body.content)
        session.add(article)
        session.commit()
        return article
    finally:
        session.close()

# 게시글 수정
@app.patch("/articles/{article_id}", response_model=ArticleRequest, status_code=status.HTTP_200_OK)
def update_article(article_id: int, body: ArticleRequest):
    session = SessionFactory()
    try:
        stmt = select(Article).where(Article.id == article_id)
        article = session.execute(stmt).scalars().first()
        if article :
            if body.title is not None:
                article.title = body.title
            if body.content is not None:
                article.content = body.content
            session.commit()
            return article
        raise HTTPException(status_code=404, detail="Article Not found.")
    finally:
        session.close()

# 게시글 삭제
@app.delete("/articles/{article_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_article(article_id: int):
    session = SessionFactory()
    try:
        stmt = select(Article).where(Article.id == article_id)
        article = session.execute(stmt).scalars().first()
        if article :
            session.delete(article)
            session.commit()
            return
        raise HTTPException(status_code=404, detail="Article Not found.")
    finally:
        session.close()

# 댓글 작성
@app.post("/articles/{article_id}/comments", response_model=CommentResponse)
def create_comment_handler(article_id: int, request: Request, body: CommentRequest):
    with SessionFactory() as session:
        #로그인 확인
        name = request.session.get("name")
        if name is None:
            raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Unauthorized")
        stmt = select(Article).where(Article.id == article_id)
        article_id = session.execute(stmt).scalars().first()

        if article_id is None:
            raise HTTPException(status_code=404, detail="Article Not found.")

        comment = Comment(author=name, content=body.content, article_id=article_id)
        session.add(comment)
        session.commit()
        session.refresh(comment)
        return comment


