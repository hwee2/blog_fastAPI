from pydantic import BaseModel

# 게시글 응답
class ArticleRequest(BaseModel):
    id : int
    title : str
    content : str
