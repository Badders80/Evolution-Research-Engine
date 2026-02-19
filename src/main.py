"""Evolution Research Engine - Main entry point"""

from fastapi import FastAPI
from scrapers.racing import RacingScraper
from social_intel.monitor import SocialMonitor
from content_ai.generator import ContentGenerator

app = FastAPI(title="Evolution Research Engine")

@app.get("/")
def root():
    return {"status": "Evolution Research Engine active"}

@app.get("/races/upcoming")
def upcoming_races():
    """Get upcoming races with Evolution horses"""
    return {"races": []}  # TODO: implement

@app.get("/social/trending")
def trending_content():
    """Get trending reel formats"""
    return {"trends": []}  # TODO: implement

@app.get("/content/ideas")
def content_ideas():
    """AI-generated content topics"""
    return {"ideas": []}  # TODO: implement

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8001)
