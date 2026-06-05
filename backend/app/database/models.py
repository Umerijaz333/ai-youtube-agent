from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Text, DateTime, Boolean, Float, ForeignKey, JSON
from datetime import datetime

Base = declarative_base()

class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True)
    email = Column(String(255), unique=True, index=True)
    username = Column(String(100), unique=True, index=True)
    hashed_password = Column(String(255))
    is_active = Column(Boolean, default=True)
    created_at = Column(DateTime, default=datetime.utcnow)

class Channel(Base):
    __tablename__ = "channels"
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    youtube_channel_id = Column(String(255), unique=True)
    channel_name = Column(String(255))
    created_at = Column(DateTime, default=datetime.utcnow)

class ContentIdea(Base):
    __tablename__ = "content_ideas"
    id = Column(Integer, primary_key=True)
    channel_id = Column(Integer, ForeignKey("channels.id"))
    topic = Column(String(500))
    search_volume = Column(Integer)
    viral_potential_score = Column(Float)
    status = Column(String(50), default="pending")
    created_at = Column(DateTime, default=datetime.utcnow)

class Script(Base):
    __tablename__ = "scripts"
    id = Column(Integer, primary_key=True)
    content_idea_id = Column(Integer, ForeignKey("content_ideas.id"))
    video_type = Column(String(50))
    script_text = Column(Text)
    created_at = Column(DateTime, default=datetime.utcnow)

class Video(Base):
    __tablename__ = "videos"
    id = Column(Integer, primary_key=True)
    channel_id = Column(Integer, ForeignKey("channels.id"))
    content_idea_id = Column(Integer, ForeignKey("content_ideas.id"))
    title = Column(String(500))
    status = Column(String(50))
    file_path = Column(String(500))
    created_at = Column(DateTime, default=datetime.utcnow)

class VideoAnalytics(Base):
    __tablename__ = "video_analytics"
    id = Column(Integer, primary_key=True)
    video_id = Column(Integer, ForeignKey("videos.id"))
    views = Column(Integer, default=0)
    watch_time_hours = Column(Float, default=0)
    ctr = Column(Float, default=0)
    created_at = Column(DateTime, default=datetime.utcnow)
