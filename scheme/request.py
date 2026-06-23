from pydantic import BaseModel

# 게시글 생성
class ArticleRequest(BaseModel):
    title: str
    content: str

# 게시글 수정
class ArticleUpdateRequest(BaseModel):
    title: str
    content: str


# 댓글 생성 요청 모델
class CommentRequest(BaseModel):
    author: str
    content: str
