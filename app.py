from base64 import b64encode
from pathlib import Path

import streamlit as st


ROOT = Path(__file__).parent

st.set_page_config(page_title="Trackside: Skyline Sprint", page_icon="🏁", layout="wide")
st.markdown(
    """
    <style>
    [data-testid="stHeader"], [data-testid="stToolbar"], footer {display: none;}
    .stApp {background: #101614;}
    .block-container {padding: 0.5rem 0.7rem 0; max-width: 1440px;}
    </style>
    """,
    unsafe_allow_html=True,
)

game_html = (ROOT / "game.html").read_text(encoding="utf-8")
for asset_name in ("runner", "train", "hurdle", "token"):
    asset = ROOT / "assets" / f"{asset_name}.svg"
    encoded_asset = b64encode(asset.read_bytes()).decode("ascii")
    game_html = game_html.replace(
        f"__{asset_name.upper()}__", f"data:image/svg+xml;base64,{encoded_asset}"
    )

st.iframe(game_html, height=850, alt="Trackside: Skyline Sprint endless runner")