import streamlit as st
from data_loader import load_table, content_for
from theme import hero, card

PLACES = ["At Home", "At School", "In the Community", "Online & Social Media"]


def show():
    hero("Take Action", "Small, safe actions you can try this week.")
    st.write("")
    intro = content_for("Take Action").iloc[0]
    st.write(intro["body"])
    df = load_table("actions")
    tabs = st.tabs(PLACES)
    for tab, place in zip(tabs, PLACES):
        with tab:
            for _, r in df[df["place"] == place].iterrows():
                card(r["title"], r["description"], r["source"], r["url"], badge=r["sdg"])
    st.subheader("Make a pledge")
    st.caption("Optional. No name, email or personal data. It lives only in this browser session and is gone when you close the page.")
    choice = st.selectbox("Pick one action", [""] + list(df["title"]), format_func=lambda x: x or "Choose an action")
    when = st.selectbox("When?", ["This week", "This month", "Every week"])
    c = st.columns(2)
    if c[0].button("Save my pledge") and choice:
        st.session_state.pledge = (choice, when)
    if c[1].button("Reset"):
        st.session_state.pop("pledge", None)
    if "pledge" in st.session_state:
        a, w = st.session_state.pledge
        st.success(f"You chose: {a} ({w.lower()}). Small actions can contribute to wider change. A pledge records your intention, not proof of impact.")
    st.subheader("Reflect")
    for q in ("What is one barrier you can help reduce?", "Who could you work with?", "How will you know whether your action helped?"):
        st.markdown(f"- {q}")
    st.caption("Try recording non-sensitive evidence, such as books collected or a study session held. Lasting progress also needs public policy, budgets, services and accountability.")
