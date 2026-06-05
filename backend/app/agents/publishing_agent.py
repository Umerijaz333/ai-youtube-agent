import logging
from app.services.youtube_service import YoutubeService

logger = logging.getLogger(__name__)
youtube_service = YoutubeService()

class PublishingAgent:
    async def publish_video(self, video_path: str, metadata: dict, schedule_time: str = None) -> str:
        logger.info(f"Publishing video: {metadata.get('title')}")
        
        video_id = await youtube_service.upload_video(
            video_path,
            metadata.get('title', 'Untitled'),
            metadata.get('description', ''),
            metadata.get('tags', [])
        )
        
        if schedule_time:
            await youtube_service.schedule_video(video_id, schedule_time)
        
        return video_id
    
    async def schedule_publishing(self, video_id: str, publish_time: str) -> bool:
        logger.info(f"Scheduling video {video_id}")
        return await youtube_service.schedule_video(video_id, publish_time)
