"""Reads content from data/unisight_db.xlsx (sheet "Website Database") and small CSV tables.
Update the Excel/CSV files, not the code."""
import json
import pandas as pd
import streamlit as st
from config import DATA

DB_FILE = DATA / "unisight_db.xlsx"
DB_SHEET = "Website Database"
SECTION_MAP = {  # Excel "Seccion" value -> section name used by the app
    "SDG 4": "SDG 4 – Quality Education",
    "SDG 5": "SDG 5 – Gender Equality",
    "Projections 2050": "Projections 2050",
    "Wireframes / What If?": "Wireframes / What If?",
    "Take Action": "Take Action",
    "Who We Are": "Who We Are",
}


@st.cache_data(show_spinner=False)
def load_db() -> pd.DataFrame:
    df = pd.read_excel(DB_FILE, sheet_name=DB_SHEET).fillna("")
    df.columns = ["id", "section", "title", "body", "source", "url"]  # by position: headers are in Spanish
    df["section"] = df["section"].map(SECTION_MAP).fillna(df["section"])
    return df


@st.cache_data(show_spinner=False)
def load_table(name: str) -> pd.DataFrame:
    return pd.read_csv(DATA / f"{name}.csv").fillna("")


@st.cache_data(show_spinner=False)
def load_stories() -> dict:
    with open(DATA / "stories.json", encoding="utf-8") as f:
        return json.load(f)


def content_for(section: str) -> pd.DataFrame:
    """Database rows of a section that have visitor-facing copy (data/visitor_copy.csv, keyed by ID).
    Rows without copy are production briefs (stats, targets, story specs) and are not shown as text."""
    db = load_db()
    copy = dict(zip(*[load_table("visitor_copy")[c] for c in ("id", "text")]))
    df = db[db["section"] == section].copy()
    df["body"] = df["id"].map(copy).fillna("")
    return df[df["body"] != ""]


def site_value(key: str) -> str:
    t = load_table("site")
    m = t[t["key"] == key]
    return str(m["value"].iloc[0]).strip() if len(m) else ""
