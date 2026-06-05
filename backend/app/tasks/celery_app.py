from celery import Celery
from app.core.config import settings

celery_app = Celery(
    'ai_youtube_agent',
    broker=settings.CELERY_BROKER_URL,
    backend=settings.CELERY_BROKER_URL
)

@celery_app.task
async def generate_content_idea(topic: str) -> dict:
    from app.agents.trend_research_agent import TrendResearchAgent
    agent = TrendResearchAgent()
    return await agent.research_trends(topic)

@celery_app.task
async def generate_script(topic: str, video_type: str) -> dict:
    from app.agents.script_writing_agent import ScriptWritingAgent
    agent = ScriptWritingAgent()
    return await agent.generate_script(topic, video_type)

@celery_app.task
async def produce_video(script: str, video_type: str) -> str:
    from app.agents.video_production_agent import VideoProductionAgent
    agent = VideoProductionAgent()
    return await agent.produce_video(script, video_type)

@celery_app.task
async def publish_video(video_path: str, metadata: dict) -> str:
    from app.agents.publishing_agent import PublishingAgent
    agent = PublishingAgent()
    return await agent.publish_video(video_path, metadata)
