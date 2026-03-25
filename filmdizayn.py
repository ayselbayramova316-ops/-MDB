import streamlit as st
import pandas as pd

st.set_page_config(
    page_title="CineSearch",
    page_icon="🎬",
    layout="wide",
)

st.markdown("""
<style>

/* ---------- global ---------- */
html, body, [data-testid="stAppViewContainer"], [data-testid="stMain"] {
    background-color: #0a1a0f !important;
    color: #c8f5a0 !important;
}
[data-testid="stSidebar"] { display: none; }
[data-testid="stHeader"]  { background: transparent; }

/* ---------- header ---------- */
.cine-header {
    background: linear-gradient(135deg, #0d2b15, #143d1e);
    border-bottom: 1px solid #1e5c2a;
    border-radius: 12px;
    padding: 18px 28px 14px;
    display: flex;
    align-items: center;
    gap: 14px;
    margin-bottom: 25px; /* 🔥 BOŞLUQ BURDA */
}

.cine-icon {
    width: 42px; height: 42px;
    background: #2ecc71;
    border-radius: 10px;
    display: flex; align-items: center; justify-content: center;
    font-size: 20px;
}

.cine-title  { font-size: 24px; font-weight: 700; }
.cine-sub    { font-size: 12px; color: #5a9e6a; }

.cine-badge  {
    margin-left: auto;
    background: #1a3d22;
    border: 1px solid #2d6e3a;
    color: #7dca8a;
    padding: 4px 12px;
    border-radius: 20px;
}

/* ---------- inputs ---------- */
[data-testid="stTextInput"] > div > div > input,
[data-testid="stSelectbox"] > div > div,
[data-testid="stMultiSelect"] > div > div {
    background-color: #0a1a0f !important;
    border: 1px solid #1e5c2a !important;
    border-radius: 8px !important;
    color: #c8f5a0 !important;
}

/* ---------- movie cards ---------- */
.movie-card {
    background: #0f2116;
    border: 1px solid #1a3d22;
    border-radius: 12px;
    padding: 14px 18px;
    margin-bottom: 10px;
    display: flex;
    justify-content: space-between;
}

.movie-title { font-size: 15px; font-weight: 600; }
.movie-meta  { font-size: 12px; color: #4a8f5a; }

</style>
""", unsafe_allow_html=True)


@st.cache_data
def load_data():
    return pd.read_csv("IMDB-Movie-Data.csv")

df = load_data()

# HEADER
st.markdown(f"""
<div class="cine-header">
    <div class="cine-icon">🎬</div>
    <div>
        <div class="cine-title">CineSearch</div>
        <div class="cine-sub">IMDB Movie Database</div>
    </div>
    <div class="cine-badge">{len(df)} films</div>
</div>
""", unsafe_allow_html=True)

# INPUTS
col1, col2 = st.columns(2)

with col1:
    text_title = st.text_input("Title")
    text_director = st.text_input("Director")

with col2:
    text_actors = st.text_input("Actors")
    year_option = st.selectbox("Year", [None] + list(df["Year"].unique()))

genre_multi = st.multiselect("Genre", [])

# BUTTON
search_clicked = st.button("Search")

# RESULTS
if search_clicked:
    filtered = df.copy()

    if text_title:
        filtered = filtered[filtered["Title"].str.contains(text_title, case=False)]

    filtered = filtered.sort_values(by="Rating", ascending=False)

    for _, row in filtered.iterrows():
        st.markdown(f"""
        <div class="movie-card">
            <div>
                <div class="movie-title">{row['Title']}</div>
                <div class="movie-meta">{row['Director']} · {row['Year']}</div>
            </div>
            <div>{row['Rating']}</div>
        </div>
        """, unsafe_allow_html=True)