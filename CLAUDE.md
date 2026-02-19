# CLAUDE.md - Evolution-Research-Engine

## What this repo is and what it solves
Evolution-Research-Engine is a research and scraping tool that collects data from various racing websites to provide up-to-date information for Evolution Stables. It solves the problem of automating data collection by scraping websites like NZTR, TAB, and Racing.com for horse profiles, race results, and other relevant information.

## Full Stack
### What IS used:
- **Python 3.12** for scraping and processing
- **Requests** for HTTP requests
- **BeautifulSoup** for HTML parsing
- **Selenium** for dynamic content (optional)
- **FastAPI** for API endpoints
- **Supabase** for database storage

### What IS NOT used:
- **Scrapy**: Not used (Requests + BeautifulSoup preferred)
- **Puppeteer**: Not used (Selenium preferred for Python)
- **MongoDB**: Not used (Supabase PostgreSQL preferred)

## Hard Coding Rules

1. **No empty placeholder files** - Implement or don't create the file
2. **Scraping must be respectful** - Follow robots.txt guidelines
3. **Data must be verified** - Check for consistency and errors
4. **Performance must be optimized** - Use async scraping where possible
5. **Error handling must be robust** - Handle scraping failures gracefully

## Project Structure
```
Evolution-Research-Engine/
├── src/
│   ├── api/              # API endpoints
│   ├── content_ai/       # AI content generation
│   ├── scrapers/         # Web scrapers
│   │   └── racing.py     # Main racing scraper
│   └── social_intel/     # Social media intelligence
├── config/               # Configuration files
├── docs/                 # Documentation
├── tests/                # Test files
├── requirements.txt      # Python dependencies
└── README.md             # Documentation
```

## Key Features
1. **Horse Profiles**: Scrapes horse profiles from various sources
2. **Race Results**: Collects race results and performance data
3. **Form Guides**: Collects form guides for upcoming races
4. **Social Intel**: Analyzes social media for racing trends
5. **API Endpoints**: Provides data via FastAPI endpoints

## Environment Variables
Required environment variables in `.env`:
```
SUPABASE_URL=
SUPABASE_ANON_KEY=
```

## WSL2 Paths
- **Project Path**: `/home/evo/projects/Evolution-Research-Engine/`
- **Windows Path**: `C:\Users\Evo\projects\Evolution-Research-Engine\`
- **Dev Server Port**: 8001 (default)

## Current Phase and Next Build Target
- **Current Phase**: Scaffolded with Placeholders
- **Next Build Target**: Implement real scraping logic and API endpoints

## Commands
- **Run Server**: `python src/main.py` (runs on port 8001)
- **Install Dependencies**: `pip install -r requirements.txt`

## Source of Truth
**All development standards are defined in 00_DNA**:
- **Build Philosophy**: `/home/evo/00_DNA/build-philosophy/Master_Config_2026.md`
- **System Prompts**: `/home/evo/00_DNA/system-prompts/PROMPT_LIBRARY.md`
- **Brand Voice**: `/home/evo/00_DNA/brand-identity/BRAND_VOICE.md`
- **Workflows**: `/home/evo/00_DNA/workflows/`

**Key Files to Reference**:
1. `/home/evo/00_DNA/AGENTS.core.md` - Universal agent rules
2. `/home/evo/00_DNA/build-philosophy/Master_Config_2026.md` - Hardware and architecture specs
3. `/home/evo/00_DNA/brand-identity/MESSAGING_CHEAT_SHEET.md` - Brand voice guidelines
