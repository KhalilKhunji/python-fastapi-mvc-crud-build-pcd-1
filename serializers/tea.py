from pydantic import BaseModel
from typing import Optional, List
from .comment import CommentSchema
from .user import UserResponseSchema

class TeaSchema(BaseModel):
  id: Optional[int] = None # This makes sure you don't have to explicitly add an id when sending json data
  name: str
  in_stock: bool
  rating: int
  user: UserResponseSchema
  comments: List[CommentSchema] = []

  class Config:
    orm_mode = True

class TeaMutation(BaseModel):
  name: str
  in_stock: bool
  rating: int
