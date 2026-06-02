import streamlit as st
import joblib
import pandas as pd

# ----------------------------
# Page Config
# ----------------------------
st.set_page_config(
    page_title="🎀 Spotify Popularity Predictor",
    page_icon="🎵",
    layout="centered"
)

# ----------------------------
# Custom Pink Styling
# ----------------------------
st.markdown("""
<style>
.main {
    background-color: #0300FF;
}

h1 {
    text-align: center;
    color: #ff4fa3;
}

.stButton > button {
    width: 100%;
    height: 70px;
    font-size: 28px;
    font-weight: bold;
    background-color: #ff69b4;
    color: white;
    border-radius: 20px;
    border: none;
}

.stButton > button:hover {
    background-color: #ff4fa3;
    color: white;
}

.result-card {
    background-color: #ffe6f2;
    padding: 20px;
    border-radius: 20px;
    text-align: center;
    font-size: 30px;
    font-weight: bold;
    color: #d63384;
    margin-top: 20px;
}
</style>
""", unsafe_allow_html=True)

# ----------------------------
# Load Model
# ----------------------------
model = joblib.load("spotify_model.pkl")

# ----------------------------
# Title
# ----------------------------
st.title("🎵 Spotify Song Popularity Predictor 🎀")

st.write("Move the sliders and predict how popular your song could be!")

# ----------------------------
# Sliders
# ----------------------------
danceability = st.slider(
    "Danceability",
    min_value=0.0,
    max_value=1.0,
    value=0.5,
    step=0.01
)

energy = st.slider(
    "Energy",
    min_value=0.0,
    max_value=1.0,
    value=0.5,
    step=0.01
)

valence = st.slider(
    "Valence",
    min_value=0.0,
    max_value=1.0,
    value=0.5,
    step=0.01
)

loudness = st.slider(
    "Loudness (dB)",
    min_value=-30.0,
    max_value=0.0,
    value=-10.0,
    step=0.1
)

tempo = st.slider(
    "Tempo",
    min_value=50.0,
    max_value=200.0,
    value=120.0,
    step=1.0
)

duration_min = st.slider(
    "Duration (minutes)",
    min_value=1.5,
    max_value=7.0,
    value=3.5,
    step=0.1
)

acousticness = st.slider(
    "Acousticness",
    min_value=0.0,
    max_value=1.0,
    value=0.5,
    step=0.01
)

# ----------------------------
# Predict Button
# ----------------------------
if st.button("🎀 Predict 🎀"):

    input_data = pd.DataFrame([[
        danceability,
        energy,
        valence,
        loudness,
        tempo,
        duration_min,
        acousticness
    ]], columns=[
        "danceability",
        "energy",
        "valence",
        "loudness",
        "tempo",
        "duration_min",
        "acousticness"
    ])

    prediction = model.predict(input_data)[0]

    st.markdown(
        f"""
        <div class="result-card">
            ⭐ Popularity Score: {prediction:.1f}
        </div>
        """,
        unsafe_allow_html=True
    )