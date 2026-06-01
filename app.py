import pickle
import streamlit as st


def load_data():
    movies = pickle.load(open("movies.pkl", "rb"))
    similarity = pickle.load(open("similarity.pkl", "rb"))
    return movies, similarity


movies, similarity = load_data()


def recommender(movie):
    movie_index = movies[movies["title"] == movie].index[0]

    distances = similarity[movie_index]

    movies_list = sorted(list(enumerate(distances)), key=lambda x: x[1], reverse=True)[
        1:6
    ]

    return [movies.iloc[i[0]]["title"] for i in movies_list]


st.set_page_config(page_title="Movie Recommender", page_icon="🎬", layout="centered")

st.title("🎬 Movie Recommender")
st.caption("Find movies similar to your favorites.")

selected_movie = st.selectbox("Choose a movie", movies["title"].values)

if st.button("Recommend", use_container_width=True):

    recommendations = recommender(selected_movie)

    st.divider()
    st.subheader("Recommended Movies")

    for movie in recommendations:
        st.write(f"• {movie}")
