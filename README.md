# Evolution Research Engine

Intelligence layer for Evolution Stables. Gathers, analyzes, and distributes racing data and social insights.

## Components

### 1. Racing Data Scrapers
- racing.com, nztr.co.nz, tab.com.au, loveracing.nz
- Race schedules, form guides, odds, results

### 2. Social Intelligence
- TikTok/Instagram/YouTube trending content monitoring
- Competitor analysis (Godolphin, Coolmore, etc.)
- Engagement pattern extraction

### 3. Content AI
- Topic generation for Evolution
- Horse profile research automation
- Race preview content suggestions

### 4. API Layer
- REST endpoints for Content Factory
- WebSocket for real-time updates
- Scheduled data refresh jobs

## Data Flow
```
Research Engine → Content Factory (topics, race data)
              → Social Dashboard (trends)
              → Syndicate Portal (form guides)
```

## Setup
1. Install dependencies: `pip install -r requirements.txt`
2. Configure APIs in `config/`
3. Run: `python src/main.py`
