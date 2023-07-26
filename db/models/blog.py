from datetime import datetime
from sqlalchemy import Column, Integer, Text, String, Boolean, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from db.base_class import Base

class Blog(Base):
    id = Column(Integer, primary_key=True)
    title = Column(String, nullable=False)
    content = Column(String, nullable=False)
    author_id = Column(Integer, ForeignKey("author.id"))
    created_at = Column(DateTime, default=datetime.now)
    is_active = Column(Boolean, default=False)

    author = relationship("Author", back_populates="blogs") 