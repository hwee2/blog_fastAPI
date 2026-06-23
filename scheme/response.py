from pydantic import BaseModel
from datetime import datetime

# 게시글 응답
class ArticleRequest(BaseModel):
    id : int
    title : str
    content : str

# 댓글 응답 모델
class CommentResponse(BaseModel):
    id : int
    author : str
    content : str
    created : datetime