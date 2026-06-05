import logging

logger = logging.getLogger(__name__)

class ThumbnailAgent:
    async def design_thumbnails(self, title: str, topic: str, count: int = 3) -> list:
        logger.info(f"Designing {count} thumbnails for: {title}")
        
        thumbnails = []
        for i in range(count):
            thumbnails.append({
                "id": i + 1,
                "design": f"Thumbnail design variant {i + 1}",
                "text": title[:30],
                "color_scheme": ["red", "white"][i % 2],
                "ctr_score": 8.5 + (i * 0.3)
            })
        
        return thumbnails
    
    async def select_best_thumbnail(self, thumbnails: list) -> dict:
        logger.info("Selecting best thumbnail")
        
        best = max(thumbnails, key=lambda x: x.get('ctr_score', 0))
        return best
