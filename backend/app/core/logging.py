import logging
from pathlib import Path

def setup_logging():
    log_path = Path("logs")
    log_path.mkdir(exist_ok=True)
    
    logging.basicConfig(
        level=logging.INFO,
        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
        handlers=[
            logging.FileHandler(log_path / "app.log"),
            logging.StreamHandler()
        ]
    )
