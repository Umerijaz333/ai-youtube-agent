from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from app.database.database import get_db
from app.database.models import ContentIdea, Channel
import logging

logger = logging.getLogger(__name__)
router = APIRouter()

@router.post("/ideas/generate")
async def generate_content_ideas(channel_id: int, db: Session = Depends(get_db)):
    logger.info(f"Generating content ideas for channel {channel_id}")
    
    channel = db.query(Channel).filter(Channel.id == channel_id).first()
    if not channel:
        raise HTTPException(status_code=404, detail="Channel not found")
    
    from app.agents.trend_research_agent import TrendResearchAgent
    agent = TrendResearchAgent()
    trends = await agent.research_trends()
    
    return {"status": "success", "ideas": trends}

@router.get("/ideas")
async def get_content_ideas(channel_id: int, db: Session = Depends(get_db)):
    logger.info(f"Fetching content ideas for channel {channel_id}")
    
    ideas = db.query(ContentIdea).filter(ContentIdea.channel_id == channel_id).all()
    return {"ideas": ideas}

@router.put("/ideas/{idea_id}")
async def update_idea_status(idea_id: int, status: str, db: Session = Depends(get_db)):
    logger.info(f"Updating idea {idea_id} status to {status}")
    
    idea = db.query(ContentIdea).filter(ContentIdea.id == idea_id).first()
    if not idea:
        raise HTTPException(status_code=404, detail="Idea not found")
    
    idea.status = status
    db.commit()
    
    return {"status": "updated", "idea": idea}
