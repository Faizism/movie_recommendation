import streamlit as st
import pickle
import requests

# Load the data
movies = pickle.load(open('movies.pkl', 'rb'))
similarity = pickle.load(open('similarity.pkl', 'rb'))
movies_list = movies['title'].values

# Title
st.header('Movie Recommender System')

# Select box
selected_movie = st.selectbox('Select a movie', movies_list)

def fetch_poster(movie_id):
    url = "https://api.themoviedb.org/3/movie/{}?api_key=9a450d16ef2a8e44c7aa792be83a43d9".format(movie_id)
    data = requests.get(url)
    data = data.json()
    poster_path = data['poster_path']
    full_path = "https://image.tmdb.org/t/p/w500/" + poster_path
    return full_path

# Recommendation
def recommend(movie):
    index = movies[movies['title'] == movie].index[0]
    distance = sorted(list(enumerate(similarity[index])), reverse=True, key=lambda vector: vector[1])
    recommend_movie = []
    recommend_poster = []
    for i in distance [1:6]:
        movies_id = movies.iloc[i[0]].id
        recommend_movie.append(movies.iloc[i[0]]['title'])
        recommend_poster.append(fetch_poster(movies_id))
    return recommend_movie, recommend_poster

if st.button('Recommend'):
    recommended_movies, movies_poster = recommend(selected_movie)
    col1, col2, col3, col4, col5 = st.columns(5)
    with col1:
        st.text(recommended_movies[0]) 
        st.image(movies_poster[0])
    with col2:
        st.text(recommended_movies[1])
        st.image(movies_poster[1])
    with col3:
        st.text(recommended_movies[2])
        st.image(movies_poster[2])
    with col4:
        st.text(recommended_movies[3])
        st.image(movies_poster[3])
    with col5:
        st.text(recommended_movies[4])
        st.image(movies_poster[4])