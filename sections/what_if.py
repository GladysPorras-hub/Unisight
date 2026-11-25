"""Interactive stories from data/stories.json. Two options per decision, branching routes, 3 endings each.
The route lives in the browser session only. Nothing is stored."""
import streamlit as st
from data_loader import load_stories
from theme import hero
from config import ASSETS


def _reset(key=None):
    st.session_state.wi = {"story": key, "node": None, "path": [], "last": ""}
    if key:
        st.session_state.wi["node"] = load_stories()[key]["start"]


def _scene(key: str, nid: str, node: dict):
    img = ASSETS / "pixel" / f"{key}_{nid}.png"
    if img.exists():
        st.image(str(img), caption=node["scene"], use_container_width=True)
    else:
        st.markdown(f'<div class="pixel" role="img" aria-label="{node["scene"]}">{node["emoji"]}</div>', unsafe_allow_html=True)
        st.caption(f"Scene: {node['scene']}")


def show():
    hero("Wireframes / What If?", "Step into a fictional story, make two-way choices and see where they lead.")
    stories = load_stories()
    if "wi" not in st.session_state:
        _reset()
    wi = st.session_state.wi

    if wi["story"] is None:  # shared menu
        st.write("")
        cols = st.columns(2)
        for col, (key, s) in zip(cols, stories.items()):
            with col:
                st.markdown(f"### {s['title']}")
                st.write(f"**{s['story']}**")
                st.caption("Fictional and educational, grounded in documented issues.")
                if st.button("Open this story", key=f"open_{key}", use_container_width=True):
                    _reset(key); st.rerun()
        return

    key = wi["story"]; s = stories[key]; nid = wi["node"]; node = s["nodes"][nid]
    kind = node.get("kind", "decision")
    top = st.columns([1, 1, 3])
    if top[0].button("Restart story", key="restart"):
        _reset(key); st.rerun()
    if top[1].button("Story menu", key="menu"):
        _reset(); st.rerun()
    if kind == "decision":
        n = len(wi["path"]) + 1
        top[2].markdown(f"**Decision {n} of {s['total']}**")
        st.progress(n / s["total"])

    _scene(key, nid, node)
    if wi["last"]:
        st.info(f"**What happened:** {wi['last']}")
    st.markdown(f"### {node['title']}")
    st.write(node["text"])

    if kind == "end":
        st.success("This ending is a consequence of your route, not a prediction.")
        st.markdown("**Your route**")
        for i, (title, label) in enumerate(wi["path"], 1):
            st.markdown(f"{i}. {title}: *{label}*")
        st.markdown(f"**Learning takeaway:** {s['takeaway']}")
        c = st.columns(2)
        if c[0].button("Replay this story", key="replay", use_container_width=True):
            _reset(key); st.rerun()
        if c[1].button("Choose another story", key="another", use_container_width=True):
            _reset(); st.rerun()
    else:
        for i, ch in enumerate(node["choices"]):
            if st.button(ch["label"], key=f"{key}_{nid}_{i}", use_container_width=True):
                if kind == "decision":
                    wi["path"].append((node["title"], ch["label"]))
                wi["last"], wi["node"] = ch["consequence"], ch["next"]
                st.rerun()
    st.caption(f"{s['disclaimer']} Source: [{s['source']}]({s['source_url']})")
