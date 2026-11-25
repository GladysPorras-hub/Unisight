# UNISIGHT

Streamlit app on SDG 4 and SDG 5. All visible text is in English.

## Run
    pip install -r requirements.txt
    streamlit run app.py

## Update content (no code changes)
- Main database: `data/unisight_db.xlsx` (sheet "Website Database": ID, Seccion, Tema, Información, Fuente, Enlace). Sources and links come from here.
- Visitor-facing text for each ID: `data/visitor_copy.csv` (the Excel "Información" column holds production briefs, so the site shows this cleaned copy).
- Figures: `data/stats.csv` (every row needs source, url and year). Targets: `targets.csv`. Actions: `actions.csv`. Projections: `comparison.csv`, `needs.csv`.
- Stories: `data/stories.json` (two options per decision, 3 endings each). Pixel art: save `assets/pixel/<story>_<node>.png`, e.g. `sdg4_n1.png`.
- Team, video, social links, review date, contact: `data/site.csv` and `data/team.csv`. Blank values stay hidden.

## Deploy
Push to GitHub and deploy on Streamlit Community Cloud (main file: `app.py`). No accounts or user data are stored.

## Quick start
- Windows: double-click `iniciar.bat`
- Mac: double-click `iniciar.command` (first time: right-click > Open)
