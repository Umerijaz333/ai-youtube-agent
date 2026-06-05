import logging
from app.services.ai_service import AIService

logger = logging.getLogger(__name__)
ai_service = AIService()

class TrendResearchAgent:
    async def research_trends(self, niche: str = "making money online") -> list:
        logger.info(f"Researching trends for: {niche}")
        
        prompt = f"""Research and identify top 5 trending topics in {niche} that would work well for YouTube videos.
        For each topic provide:
        - Topic title
        - Search volume estimate
        - Competition level (Low/Medium/High)
        - Viral potential (1-10)
        
        Return as JSON array."""
        
        result = await ai_service.generate_with_openai(prompt)
        return result
    
    async def analyze_keywords(self, topic: str) -> dict:
        logger.info(f"Analyzing keywords for: {topic}")
        
        prompt = f"""For the YouTube topic '{topic}', provide:
        - 10 primary keywords
        - 10 long-tail keywords
        - Search volume estimates
        - Competition analysis
        
        Format as JSON."""
        
        result = await ai_service.generate_with_openai(prompt)
        return {"keywords": result}
