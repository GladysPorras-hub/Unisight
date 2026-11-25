import streamlit as st
from config import ASSETS
from data_loader import content_for, load_table, load_db, site_value
from theme import hero


def show():
    hero("Who We Are", "A student project about quality education and gender equality.")
    st.write("")
    name, intro = site_value("team_name"), site_value("team_intro")
    if name or intro:
        st.markdown(f"### {name}")
        st.write(intro)
    st.write(content_for("Who We Are").iloc[0]["body"])

    team = load_table("team")
    if len(team):
        cols = st.columns(3)
        for i, r in team.iterrows():
            with cols[i % 3]:
                p = ASSETS / "logos" / str(r["photo"])
                if r["photo"] and p.exists():
                    st.image(str(p), caption=r["name"])
                st.markdown(f"**{r['name']}**  \n{r['role']}")
                st.caption(r["bio"])

    if site_value("video_url"):
        st.subheader(site_value("video_title") or "Presentation video")
        st.video(site_value("video_url"))
    links = [(l, site_value(k)) for l, k in (("Instagram", "instagram"), ("TikTok", "tiktok")) if site_value(k)]
    if links:
        for col, (l, u) in zip(st.columns(len(links)), links):
            col.link_button(l, u)

    st.info("UNISIGHT is an educational student project. It is not an official United Nations website and does not provide legal, medical or emergency services.")
    bits = [b for b in (f"Content last reviewed: {site_value('review_date')}" if site_value("review_date") else "",
                        f"Contact: {site_value('contact')}" if site_value("contact") else "") if b]
    if bits:
        st.caption(" · ".join(bits))
    with st.expander("Verify at the original sources"):
        db = load_db()
        seen = set()
        for _, r in db.iterrows():
            if r["url"] and r["url"].startswith("http") and r["url"] not in seen:
                seen.add(r["url"])
                st.markdown(f"- [{r['source'] or r['url']}]({r['url']})")
