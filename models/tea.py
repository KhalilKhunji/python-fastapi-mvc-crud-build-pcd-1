# models/tea.py
from sqlalchemy import Column, Integer, String, Boolean, ForeignKey
from sqlalchemy.orm import relationship  # Import the relationship function from SQLAlchemy ORM
from .base import BaseModel  # Import the base model for SQLAlchemy
from .comment import CommentModel  # Import the CommentModel class for establishing relationships
from .user import UserModel

# Update Base to BaseModel
class TeaModel(BaseModel):

    __tablename__ = "teas"

    id = Column(Integer, primary_key=True, index=True)

    # Specific columns for our Tea Table.
    name = Column(String, unique=True)
    in_stock = Column(Boolean)
    rating = Column(Integer)

    user_id = Column(Integer, ForeignKey('users.id'))

    user = relationship('UserModel', back_populates='teas')

    # Define a relationship with the CommentModel table
    comments = relationship("CommentModel", back_populates="tea")
