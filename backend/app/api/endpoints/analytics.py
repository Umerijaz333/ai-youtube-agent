from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.database.database import get_db
from app.database.models import VideoAnalytics
import logging

logger = logging.getLogger(__name__)
router = APIRouter()

@router.get("/video/{video_id}")
async def get_video_analytics(video_id: int, db: Session = Depends(get_db)):
    logger.info(f"Fetching analytics for video {video_id}")
    
    analytics = db.query(VideoAnalytics).filter(VideoAnalytics.video_id == video_id).first()
    if not analytics:
        return {"message": "No analytics yet"}
    
    return analytics

@router.get("/channel/{channel_id}")
async def get_channel_analytics(channel_id: int, db: Session = Depends(get_db)):
    logger.info(f"Fetching channel analytics {channel_id}")
    
    from sqlalchemy import func
    from app.database.models import Video
    
    stats = db.query(
        func.sum(VideoAnalytics.views),
        func.sum(VideoAnalytics.watch_time_hours),
        func.avg(VideoAnalytics.ctr)
    ).join(Video).filter(Video.channel_id == channel_id).first()
    
    return {"total_views": stats[0], "total_watch_time": stats[1], "avg_ctr": stats[2]}
