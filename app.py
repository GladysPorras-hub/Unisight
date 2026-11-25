import streamlit as st
from config import SECTIONS, ASSETS
import theme
from sections import sdg4, sdg5, projections, what_if, take_action, who_we_are

st.set_page_config(page_title="UNISIGHT", page_icon="🔴", layout="wide")
theme.inject()

PAGES = dict(zip(SECTIONS, [sdg4.show, sdg5.show, projections.show, what_if.show, take_action.show, who_we_are.show]))

with st.sidebar:
    logo = ASSETS / "logos" / "unisight.png"
    if logo.exists():
        st.image(str(logo))
    else:
        st.markdown("## UNISIGHT")
    choice = st.radio("Explore", SECTIONS, label_visibility="collapsed")
    st.caption("No accounts. No data stored.")

PAGES[choice]()
