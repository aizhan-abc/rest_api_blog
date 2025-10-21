from sqlalchemy import Column, Integer, String, Text, DateTime, func
from .database import Base

class Post(Base):
    __tablename__ = "posts"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(200), nullable=False)
    content = Column(Text, nullable=False)
    author = Column(String(100), nullable=False)
    likes = Column(Integer, default=0)   # 🆕 added this line
    created_at = Column(DateTime(timezone=True), server_default=func.now())
