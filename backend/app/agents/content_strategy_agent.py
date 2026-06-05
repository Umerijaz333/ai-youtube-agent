import logging
from app.services.ai_service import AIService

logger = logging.getLogger(__name__)
ai_service = AIService()

class ContentStrategyAgent:
    async def develop_strategy(self, topic: str, keywords: list) -> dict:
        logger.info(f"Developing content strategy for: {topic}")
        
        prompt = f"""Create a content strategy for a YouTube video about '{topic}'.
        Keywords: {', '.join(keywords)}
        
        Provide:
        - Content angle
        - Target audience
        - Best video length (short/long form)
        - Suggested sections
        - CTAs
        - SEO optimization tips
        
        Return as JSON."""
        
        result = await ai_service.generate_with_openai(prompt)
        return {"strategy": result}
    
    async def estimate_viral_potential(self, topic: str, keywords: list) -> float:
        logger.info(f"Estimating viral potential for: {topic}")
        
        prompt = f"""Rate the viral potential of a YouTube video about '{topic}' on a scale of 1-10.
        Keywords: {', '.join(keywords)}
        
        Consider:
        - Trending nature
        - Emotional appeal
        - Shareability
        - Current search trends
        
        Provide only a number."""
        
        result = await ai_service.generate_with_openai(prompt)
        try:
            return float(result.strip())
        except:
            return 5.0
