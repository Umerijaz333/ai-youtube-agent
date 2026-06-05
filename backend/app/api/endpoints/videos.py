from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database.database import get_db
from app.database.models import Video, Channel
import logging

logger = logging.getLogger(__name__)
router = APIRouter()

@router.post("/generate")
async def generate_video(channel_id: int, script_id: int, db: Session = Depends(get_db)):
    logger.info(f"Generating video from script {script_id}")
    
    from app.agents.video_production_agent import VideoProductionAgent
    agent = VideoProductionAgent()
    
    video_path = await agent.produce_video("sample_script", "long_form")
    
    return {"status": "generating", "video_path": video_path}

@router.get("/{video_id}")
async def get_video(video_id: int, db: Session = Depends(get_db)):
    logger.info(f"Fetching video {video_id}")
    
    video = db.query(Video).filter(Video.id == video_id).first()
    if not video:
        raise HTTPException(status_code=404, detail="Video not found")
    
    return video

@router.get("")
async def list_videos(channel_id: int, db: Session = Depends(get_db)):
    logger.info(f"Listing videos for channel {channel_id}")
    
    videos = db.query(Video).filter(Video.channel_id == channel_id).all()
    return {"videos": videos}
