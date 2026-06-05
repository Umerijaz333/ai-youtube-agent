import logging
from app.core.config import settings
import openai
import anthropic
import google.generativeai as genai

logger = logging.getLogger(__name__)

class AIService:
    def __init__(self):
        if settings.OPENAI_API_KEY:
            openai.api_key = settings.OPENAI_API_KEY
        if settings.CLAUDE_API_KEY:
            self.claude_client = anthropic.Anthropic(api_key=settings.CLAUDE_API_KEY)
        if settings.GEMINI_API_KEY:
            genai.configure(api_key=settings.GEMINI_API_KEY)
    
    async def generate_with_openai(self, prompt: str, max_tokens: int = 2000) -> str:
        try:
            response = openai.ChatCompletion.create(
                model=settings.OPENAI_MODEL,
                messages=[{"role": "user", "content": prompt}],
                max_tokens=max_tokens
            )
            return response.choices[0].message.content
        except Exception as e:
            logger.error(f"OpenAI error: {e}")
            return ""
    
    async def generate_with_claude(self, prompt: str) -> str:
        try:
            message = self.claude_client.messages.create(
                model=settings.CLAUDE_MODEL,
                max_tokens=2000,
                messages=[{"role": "user", "content": prompt}]
            )
            return message.content[0].text
        except Exception as e:
            logger.error(f"Claude error: {e}")
            return ""
    
    async def generate_with_gemini(self, prompt: str) -> str:
        try:
            model = genai.GenerativeModel(settings.GEMINI_API_KEY)
            response = model.generate_content(prompt)
            return response.text
        except Exception as e:
            logger.error(f"Gemini error: {e}")
            return ""
