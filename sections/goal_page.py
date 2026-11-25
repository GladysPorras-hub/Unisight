"""Shared layout for SDG 4 and SDG 5 pages: text from the database, figures, official targets."""
import streamlit as st
from data_loader import content_for, load_table
from theme import hero, card
from sections.stats_view import show_stats


def render(section: str, goal: int, tagline: str):
    hero(section, tagline)
    st.write("")
    for _, r in content_for(section).iterrows():
        card(r["title"], r["body"], r["source"], r["url"])

    st.subheader("The numbers")
    show_stats(goal)

    st.subheader(f"SDG {goal} targets")
    t = load_table("targets")
    for _, r in t[t["goal"] == goal].iterrows():
        with st.expander(f"Target {r['target']}"):
            st.write(r["summary"])
    base = f"https://sdgs.un.org/goals/goal{goal}"
    st.caption(f"Official wording: [United Nations — Goal {goal}]({base})")
