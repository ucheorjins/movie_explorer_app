import streamlit as st
import pandas as pd

# Load your data
df = pd.read_csv("final_movie_info.csv")

st.set_page_config(page_title="🎬 Movie Search", layout="wide")
st.title("Top 300 Movie of All Time (Maybe)")

# Safely convert datatypes
df["year"] = df["year"].astype(str).str.extract(r"(\d{4})").astype(float)
df["RT rating (%)"] = pd.to_numeric(df["RT rating (%)"], errors="coerce")
df["imdb rating"] = pd.to_numeric(df["imdb rating"], errors="coerce")
df["runtime (minutes)"] = pd.to_numeric(df["runtime (minutes)"], errors="coerce")
df["genre"] = df["genre"].fillna("")

# Filter sidebar
# --- Sidebar filters ---
with st.sidebar.form("filter_form"):
    st.subheader("🎯 Filter Movies")

    title_query = st.text_input("Search by Title", value=st.session_state.get("title_query", ""))
    genre_query = st.text_input("Search by Genre", value=st.session_state.get("genre_query", ""))

    year_min, year_max = st.slider("Year Range", int(df["year"].min()), int(df["year"].max()),
                                   value=st.session_state.get("year_range", (int(df["year"].min()), int(df["year"].max()))))
    
    rt_min, rt_max = st.slider("RT Rating %", 0, 100, value=(0, 100))
    imdb_min, imdb_max = st.slider("IMDb Rating", 0.0, 10.0, value=(0.0, 10.0))
    runtime_min, runtime_max = st.slider("Runtime (min)", 0, int(df["runtime (minutes)"].max()), value=(0, int(df["runtime (minutes)"].max())))

    col1, col2 = st.columns([1, 1])
    search_btn = col1.form_submit_button("🔍 Search")
    clear_btn = col2.form_submit_button("🧹 Clear Filters")

# Handle form behavior
if clear_btn:
    st.session_state["title_query"] = ""
    st.session_state["genre_query"] = ""
    st.session_state["year_range"] = (int(df["year"].min()), int(df["year"].max()))
    st.rerun()

if search_btn:
    st.session_state["title_query"] = title_query
    st.session_state["genre_query"] = genre_query
    st.session_state["year_range"] = (year_min, year_max)


# Filter logic
filtered = df.copy()

# --Fill missing values so comparisons don’t break--
filtered["year"] = filtered["year"].fillna(0)
filtered["RT rating (%)"] = filtered["RT rating (%)"].fillna(0)
filtered["imdb rating"] = filtered["imdb rating"].fillna(0)
filtered["runtime (minutes)"] = filtered["runtime (minutes)"].fillna(0)
filtered["genre"] = filtered["genre"].fillna("")

# --Title search (optional)--
if title_query:
    filtered = filtered[filtered["title"].str.contains(title_query, case=False, na=False)]

# --Genre search (optional)--
if genre_query:
    filtered = filtered[filtered["genre"].str.lower().str.contains(genre_query.lower())]

# --Numeric filters (always apply, using sliders)--
filtered = filtered[
    (filtered["year"] >= year_min) & (filtered["year"] <= year_max) &
    (filtered["RT rating (%)"] >= rt_min) & (filtered["RT rating (%)"] <= rt_max) &
    (filtered["imdb rating"] >= imdb_min) & (filtered["imdb rating"] <= imdb_max) &
    (filtered["runtime (minutes)"] >= runtime_min) & (filtered["runtime (minutes)"] <= runtime_max)
]

#To show all movies and increment index
st.write(f"🎞️ Showing {len(filtered)} movies:")
filtered.index = filtered.index + 1
st.dataframe(filtered)


# Export
csv = filtered.to_csv(index=False).encode("utf-8")
st.download_button("📥 Download results as CSV", csv, "filtered_movies.csv", "text/csv")

