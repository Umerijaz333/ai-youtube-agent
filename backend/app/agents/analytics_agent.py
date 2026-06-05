import logging
from app.services.analytics_service import AnalyticsService

logger = logging.getLogger(__name__)
analytics_service = AnalyticsService()

class AnalyticsAgent:
    async def track_video_performance(self, video_id: str) -> dict:
        logger.info(f"Tracking performance for video {video_id}")
        
        metrics = await analytics_service.get_video_metrics(video_id)
        return metrics
    
    async def generate_insights(self, metrics: dict) -> dict:
        logger.info("Generating performance insights")
        
        insights = {
            "performance_level": "good" if metrics.get('views', 0) > 1000 else "starting",
            "recommendations": [
                "Improve thumbnail based on CTR",
                "Optimize upload frequency",
                "Enhance script with more hooks"
            ]
        }
        
        return insights
