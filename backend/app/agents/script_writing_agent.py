import logging
from app.services.ai_service import AIService

logger = logging.getLogger(__name__)
ai_service = AIService()

class ScriptWritingAgent:
    async def generate_script(self, topic: str, video_type: str = "long_form", duration: int = 600) -> dict:
        logger.info(f"Generating {video_type} script for: {topic}")
        
        if video_type == "long_form":
            prompt = f"""Write a compelling 8-15 minute YouTube script about '{topic}'.
            
            Include:
            - Hook (first 10 seconds)
            - Introduction
            - 3-4 main points with stories
            - Call to action
            - Outro
            
            Make it engaging, conversational, and optimized for retention.
            Return as JSON with sections."""
        else:
            prompt = f"""Write a 30-60 second YouTube Short script about '{topic}'.
            
            Include:
            - Eye-catching hook
            - Quick value proposition
            - Call to action
            
            Make it punchy and viral-worthy."""
        
        result = await ai_service.generate_with_claude(prompt)
        return {"script": result, "type": video_type}
    
    async def optimize_for_seo(self, script: str, keywords: list) -> dict:
        logger.info("Optimizing script for SEO")
        
        prompt = f"""Optimize this YouTube script for SEO.
        Script: {script}
        Target keywords: {', '.join(keywords)}
        
        Provide:
        - Optimized title
        - SEO description
        - Tags (10-15)
        - Chapters
        
        Return as JSON."""
        
        result = await ai_service.generate_with_openai(prompt)
        return {"seo_data": result}
