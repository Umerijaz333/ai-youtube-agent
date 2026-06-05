from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database.database import get_db
from app.database.models import Video
import logging

logger = logging.getLogger(__name__)
router = APIRouter()

@router.post("/video/{video_id}")
async def publish_video(video_id: int, db: Session = Depends(get_db)):
    logger.info(f"Publishing video {video_id}")
    
    video = db.query(Video).filter(Video.id == video_id).first()
    if not video:
        raise HTTPException(status_code=404, detail="Video not found")
    
    video.status = "published"
    db.commit()
    
    return {"status": "published", "video_id": video_id}

@router.post("/schedule")
async def schedule_video(video_id: int, publish_time: str, db: Session = Depends(get_db)):
    logger.info(f"Scheduling video {video_id} for {publish_time}")
    
    video = db.query(Video).filter(Video.id == video_id).first()
    if not video:
        raise HTTPException(status_code=404, detail="Video not found")
    
    return {"status": "scheduled", "publish_time": publish_time}
