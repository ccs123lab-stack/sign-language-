# Trackside: Skyline Sprint

An original, single-player 3D endless runner built with Streamlit and Three.js. Switch between three lanes, jump over barriers, slide under signs, and collect tokens as the city speeds up. The browser loads Three.js from jsDelivr, so an internet connection is required to play.

## Run locally

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
streamlit run app.py
```

Open the local URL printed by Streamlit. Use the arrow keys or A/D to move, Up/W/Space to jump, Down/S to slide, and P to pause. Touch controls are available on narrow screens. Your best distance is saved in the browser.

## Deploy

Create a Streamlit Community Cloud app from this repository, select `main` as the branch, and set `app.py` as the main file. The dependencies are listed in `requirements.txt`.