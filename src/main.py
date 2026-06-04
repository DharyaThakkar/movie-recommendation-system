import json
import streamlit as st
from recommend import df, recommend_movies
from omdb_utils import get_movie_details

# ----------------------------
# Config
# ----------------------------
config = json.load(open("config.json"))
OMDB_API_KEY = config["OMDB_API_KEY"]

st.set_page_config(
    page_title="Movie Recommendation System",
    page_icon="🎬",
    layout="wide"
)

# ----------------------------
# Cache OMDb Requests
# ----------------------------
@st.cache_data(show_spinner=False)
def fetch_movie_details(title):
    return get_movie_details(title, OMDB_API_KEY)

# ----------------------------
# Sidebar
# ----------------------------
with st.sidebar:
    st.title("🎬 Movie Recommender")

    st.markdown("---")

    st.metric("Movies in Dataset", len(df))

    st.markdown("""
    ### Technologies Used

    - TF-IDF Vectorization
    - Cosine Similarity
    - NLTK
    - Streamlit
    - OMDb API
    """)

    st.markdown("---")

    st.info(
        "Select a movie and discover similar recommendations."
    )

# ----------------------------
# Header
# ----------------------------
st.markdown(
    """
    <h1 style='text-align:center'>
        🎬 Movie Recommendation System
    </h1>
    <p style='text-align:center;font-size:18px'>
        Find movies similar to your favorites using Machine Learning
    </p>
    """,
    unsafe_allow_html=True
)

st.markdown("---")

# ----------------------------
# Movie Selection
# ----------------------------
movie_list = sorted(df['title'].dropna().unique())

selected_movie = st.selectbox(
    "🎥 Select a Movie",
    movie_list
)

# ----------------------------
# Selected Movie Details
# ----------------------------
plot, poster = fetch_movie_details(selected_movie)

st.subheader("Selected Movie")

col1, col2 = st.columns([1, 3])

with col1:
    if poster != "N/A":
        st.image(poster, use_container_width=True)

with col2:
    st.markdown(f"## {selected_movie}")

    if plot != "N/A":
        st.write(plot)
    else:
        st.write("Plot not available.")

st.markdown("---")

# ----------------------------
# Recommendations
# ----------------------------
if st.button("🚀 Recommend Similar Movies", use_container_width=True):

    with st.spinner("Finding similar movies..."):

        recommendations = recommend_movies(selected_movie)

    if recommendations is None or recommendations.empty:
        st.warning("No recommendations found.")
    else:

        st.success("Top 5 Similar Movies")

        cols = st.columns(5)

        for idx, (_, row) in enumerate(recommendations.iterrows()):

            movie_title = row["title"]

            rec_plot, rec_poster = fetch_movie_details(movie_title)

            with cols[idx]:

                if rec_poster != "N/A":
                    st.image(
                        rec_poster,
                        use_container_width=True
                    )

                st.markdown(
                    f"""
                    <div style='text-align:center;font-weight:bold;min-height:60px'>
                    {movie_title}
                    </div>
                    """,
                    unsafe_allow_html=True
                )

                with st.expander("Show Plot"):
                    if rec_plot != "N/A":
                        st.write(rec_plot)
                    else:
                        st.write("Plot not available.")