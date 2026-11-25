import streamlit as st
from data_loader import content_for, load_table
from theme import hero, card

CHAIN = ["Quality learning", "Skills and knowledge of rights", "Fair opportunity", "Shared participation", "Community well-being"]


def _row(rows, rid):
    r = rows[rows["id"] == rid].iloc[0]
    return r


def show():
    hero("Projections 2050", "Two possible futures. Not forecasts, not official UN projections.")
    rows = content_for("Projections 2050")
    st.write("")
    r = _row(rows, "DB025")
    card(r["title"], r["body"], r["source"], r["url"])

    tabs = st.tabs(["Two futures", "What could change", "How the goals connect", "Compare"])
    with tabs[0]:
        a, b = st.columns(2)
        with a:
            r = _row(rows, "DB026"); st.markdown("##### If progress accelerates"); card("Hypothetical scenario", r["body"], r["source"], r["url"])
        with b:
            r = _row(rows, "DB027"); st.markdown("##### If barriers persist"); card("Hypothetical scenario", r["body"], r["source"], r["url"])
        st.caption("Scenarios, not predictions.")
    with tabs[1]:
        for rid, name in (("DB028", "Education"), ("DB029", "Gender equality")):
            r = _row(rows, rid); card(f"How {name.lower()} could change by 2050", r["body"], r["source"], r["url"])
    with tabs[2]:
        r = _row(rows, "DB030"); st.write(r["body"])
        step = st.select_slider("Follow the chain", CHAIN, value=CHAIN[0])
        i = CHAIN.index(step)
        st.progress((i + 1) / len(CHAIN), text=" → ".join(f"**{c}**" if c == step else c for c in CHAIN))
        st.caption(f"Source: [{r['source']}]({r['url']})")
    with tabs[3]:
        cmp = load_table("comparison")
        pick = st.radio("Choose a future", ["If progress accelerates", "If barriers persist"], horizontal=True)
        col = "accelerates" if pick.endswith("accelerates") else "persists"
        for _, c in cmp.iterrows():
            card(c["dimension"], c[col])
        with st.expander("What would need to happen?"):
            for _, n in load_table("needs").iterrows():
                st.markdown(f"- {n['item']}")
        st.caption("Qualitative descriptions. These are not official UN forecasts and carry no 2050 percentages.")
