#!/usr/bin/env python3
"""
Evolution Research Engine - Main API Server
FastAPI endpoints for Content Factory integration
"""

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List, Optional
import json
from datetime import datetime

# Import scrapers
from src.scrapers.racing import NZTRScraper, RacingComScraper, TABScraper, ContentGenerator

app = FastAPI(
    title="Evolution Research Engine",
    description="Intelligence layer for Evolution Stables content production",
    version="1.0.0"
)

# Initialize scrapers
nztr = NZTRScraper()
racing_com = RacingComScraper()
tab = TABScraper()
content_gen = ContentGenerator()

class HorseProfile(BaseModel):
    name: str
    age: int
    sex: str
    trainer: str
    sire: str
    dam: str
    record: str

class RacePreview(BaseModel):
    hook: str
    angle: str
    key_points: List[str]
    cta: str

class ContentIdea(BaseModel):
    type: str
    title: str
    hook: str
    suggested_scenes: List[str]

@app.get("/")
def root():
    return {
        "service": "Evolution Research Engine",
        "status": "active",
        "endpoints": [
            "/races/upcoming",
            "/horses/{name}",
            "/content/ideas",
            "/content/race-preview/{horse_name}"
        ]
    }

@app.get("/races/upcoming")
def upcoming_races(days: int = 7):
    """Get upcoming races with Evolution horses"""
    try:
        races = nztr.get_upcoming_races(days)
        return {
            "races": races,
            "generated_at": datetime.now().isoformat()
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/horses/{name}")
def horse_profile(name: str):
    """Get detailed horse profile"""
    try:
        profile = nztr.get_horse_profile(name)
        form = racing_com.get_form_guide(name)
        return {
            "profile": profile,
            "form": form,
            "content_suggestions": content_gen.generate_horse_profile(profile)
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/content/race-preview/{horse_name}")
def race_preview(horse_name: str):
    """Generate race preview content"""
    try:
        horse = nztr.get_horse_profile(horse_name)
        race_data = nztr.get_upcoming_races(1)
        preview = content_gen.generate_race_preview(horse_name, race_data)
        return preview
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/content/ideas")
def content_ideas():
    """Generate content ideas for Evolution Stables"""
    ideas = [
        {
            "type": "horse_profile",
            "title": "Meet the Evolution Team",
            "hook": "Grounded in tradition. Evolved through innovation.",
            "suggested_scenes": ["Opening pedigree", "Training footage", "Race highlights", "CTA"]
        },
        {
            "type": "race_preview", 
            "title": "Weekend Preview",
            "hook": "The numbers don't lie",
            "suggested_scenes": ["Form guide", "Track conditions", "Jockey stats", "Prediction"]
        },
        {
            "type": "syndicate_update",
            "title": "Owner's Update",
            "hook": "Your horse, your journey",
            "suggested_scenes": ["Training update", "Health report", "Next race", "Owner benefits"]
        }
    ]
    return {"ideas": ideas, "generated_at": datetime.now().isoformat()}

@app.get("/social/trends")
def social_trends():
    """Get trending content formats"""
    # TODO: Implement social media monitoring
    return {
        "trending_formats": [
            "Quick cuts with beat drops (2-3s per scene)",
            "Before/After training comparisons",
            "Pedigree deep-dives with animated charts",
            "Race day behind-the-scenes"
        ],
        "viral_hooks": [
            "The horse the bookies fear",
            "Owned by the people",
            "Heritage meets innovation"
        ]
    }

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8001)
