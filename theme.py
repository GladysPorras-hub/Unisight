import streamlit as st
from config import *

CSS = f"""
<style>
@import url('https://fonts.googleapis.com/css2?family=Space+Grotesk:wght@500;700&family=Inter:wght@400;500&display=swap');
html, body, [class*="css"] {{ font-family:'Inter',sans-serif; color:{SLATE}; }}
h1,h2,h3 {{ font-family:'Space Grotesk',sans-serif; letter-spacing:-0.02em; }}
.hero {{ background:{SLATE}; color:{BONE}; padding:2.2rem 2rem; border-radius:6px; border-left:10px solid {CRIMSON}; }}
.hero h1 {{ color:{BONE}; margin:0 0 .4rem; font-size:2.4rem; }}
.hero p {{ color:{SAND}; margin:0; max-width:60ch; }}
.card {{ background:{SAND}; padding:1.1rem 1.3rem; border-radius:6px; border-top:4px solid {CORAL}; margin-bottom:1rem; }}
.card p {{ margin:.2rem 0 .5rem; line-height:1.55; max-width:75ch; }}
.card h4 {{ margin:0 0 .3rem; }}
.badge {{ background:{CRIMSON}; color:{BONE}; font-size:.72rem; padding:.1rem .5rem; border-radius:3px; vertical-align:middle; }}
.src {{ font-size:.8rem; opacity:.75; }}
.pixel {{ image-rendering:pixelated; font-size:4rem; background:{SLATE}; text-align:center; padding:1.5rem; border-radius:4px; border-bottom:6px solid {CORAL}; }}
.stButton>button {{ border-radius:4px; border:2px solid {CRIMSON}; background:{BONE}; color:{CRIMSON}; font-weight:600; transition:all .15s; }}
.stButton>button:hover {{ background:{CRIMSON}; color:{BONE}; }}
.stButton>button:focus-visible {{ outline:3px solid {CORAL}; }}
@media (prefers-reduced-motion: reduce) {{ * {{ transition:none !important; animation:none !important; }} }}
</style>
"""


def inject():
    st.markdown(CSS, unsafe_allow_html=True)


def hero(title: str, subtitle: str):
    st.markdown(f'<div class="hero"><h1>{title}</h1><p>{subtitle}</p></div>', unsafe_allow_html=True)


def card(title: str, body: str, source: str = "", url: str = "", badge: str = ""):
    src = f'<div class="src">Source: <a href="{url}" target="_blank" rel="noopener">{source}</a></div>' if source and url else ""
    tag = f'<span class="badge">{badge}</span> ' if badge else ""
    st.markdown(f'<div class="card"><h4>{tag}{title}</h4><p>{body}</p>{src}</div>', unsafe_allow_html=True)
