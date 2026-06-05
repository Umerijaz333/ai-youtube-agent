import logging
from app.services.video_service import VideoService

logger = logging.getLogger(__name__)
video_service = VideoService()

class VideoProductionAgent:
    async def produce_video(self, script: str, video_type: str) -> str:
        logger.info(f"Starting video production for {video_type}")
        
        # Generate video
        video_path = await video_service.generate_video(script, video_type)
        
        # Add voiceover
        video_path = await video_service.add_voiceover(video_path, "audio.mp3")
        
        # Add subtitles
        video_path = await video_service.add_subtitles(video_path, script)
        
        logger.info(f"Video production completed: {video_path}")
        return video_path
    
    async def export_video(self, video_path: str, resolution: str = "1080p") -> str:
        logger.info(f"Exporting video in {resolution}")
        return video_path
