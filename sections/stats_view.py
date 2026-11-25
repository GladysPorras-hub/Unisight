"""Draws the sourced statistics of one goal from data/stats.csv."""
import streamlit as st
import plotly.graph_objects as go
from config import *
from data_loader import load_table


def _fmt(v):
    return f"{v:g}"


def show_stats(goal: int):
    df = load_table("stats")
    df = df[df["goal"] == goal]
    for group in dict.fromkeys(df["group"]):
        g = df[df["group"] == group]
        st.markdown(f"#### {group}")
        total = g[g["indicator"] == "Total"]
        rest = g[g["indicator"] != "Total"]
        for _, r in total.iterrows():
            st.metric(f"{r['indicator']} ({r['year']}, {r['type']})", f"{_fmt(r['value'])} {r['unit']}")
        if len(rest) >= 2:
            fig = go.Figure(go.Bar(x=rest["indicator"], y=rest["value"], marker_color=CRIMSON,
                                   text=[f"{_fmt(v)} {rest['unit'].iloc[0]}" for v in rest["value"]], textposition="outside"))
            fig.update_layout(plot_bgcolor=BONE, paper_bgcolor=BONE, font_color=SLATE, height=320,
                              yaxis_title=rest["unit"].iloc[0], margin=dict(t=20))
            st.plotly_chart(fig, use_container_width=True)
        elif len(rest) == 1:
            r = rest.iloc[0]
            st.metric(f"{r['indicator']} ({r['year']})", f"{_fmt(r['value'])} {r['unit']}")
        notes = " ".join(n for n in dict.fromkeys(g["note"]) if n)
        first = g.iloc[0]
        label = "Estimate" if (g["type"] == "estimate").any() else "Reported data"
        st.markdown(f'<div class="src">{label}. {notes} Source: <a href="{first["url"]}" target="_blank" rel="noopener">{first["source"]}</a></div>', unsafe_allow_html=True)
        st.write("")
