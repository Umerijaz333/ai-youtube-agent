import logging
from app.services.ai_service import AIService

logger = logging.getLogger(__name__)
ai_service = AIService()

class SEOAgent:
    async def optimize_metadata(self, title: str, script: str, keywords: list) -> dict:
        logger.info("Optimizing YouTube metadata")
        
        prompt = f"""Optimize YouTube metadata:
        Title: {title}
        Keywords: {', '.join(keywords)}
        
        Provide JSON with:
        - Optimized title
        - Description
        - Tags
        - Hashtags"""
        
        result = await ai_service.generate_with_openai(prompt)
        return {"metadata": result}
    
    async def generate_chapters(self, script: str) -> list:
        logger.info("Generating video chapters")
        
        prompt = f"""From this script, create YouTube video chapters:
        {script}
        
        Return as JSON array with timestamp and title."""
        
        result = await ai_service.generate_with_openai(prompt)
        return {"chapters": result}
