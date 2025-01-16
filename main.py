import streamlit as st
import pickle
import requests

from PIL import Image
import io

# Load the movies data and similarity matrix
movies = pickle.load(open('movies.pkl', 'rb'))  # Load movie data from a pickle file
similarity = pickle.load(open('similarity.pkl', 'rb'))  # Load similarity matrix from a pickle file
movies_list = movies['title'].values  # Extract the list of movie titles

# Function to download an image from a URL and resize it
def resize_image(image_url, max_width=500, max_height=500):
    # Download the image from the given URL
    response = requests.get(image_url)
    if response.status_code == 200:  # Check if the request is successful
        img = Image.open(io.BytesIO(response.content))  # Open the image from byte stream
        img.thumbnail((max_width, max_height))  # Resize the image while maintaining aspect ratio
        img_bytes = io.BytesIO()
        img.save(img_bytes, format='PNG')  # Save the resized image to a byte stream
        img_bytes.seek(0)  # Reset the byte stream position
        return img_bytes  # Return the resized image as bytes
    else:
        raise Exception("Failed to download image from URL")  # Raise an error if the download fails

# Function to fetch the poster of a movie using its movie ID
def fetch_poster(movie_id):
    url = f"https://api.themoviedb.org/3/movie/{movie_id}?api_key=03b5b5a317ec4deeb7076a3d3c49b3d1"
    data = requests.get(url)
    data = data.json()
    poster_path = data.get('poster_path')  # Safely get the poster path, if available
    if poster_path:
        full_path = "https://image.tmdb.org/t/p/w500" + poster_path  # Construct the full poster URL
        return full_path
    else:
        return None  # Return None if no poster is available

# Function to recommend movies based on the selected movie
def recommend(movie):
    index = movies[movies['title'] == movie].index[0]  # Get the index of the selected movie
    distance = sorted(list(enumerate(similarity[index])), reverse=True, key=lambda vector: vector[1])  # Sort movies by similarity score

    # Lists to store recommendation details
    recommend_movie = []
    recommend_genre = []
    recommend_popularity = []
    recommend_rating = []
    recommend_releasedate = []
    recommend_overview = []
    recommend_poster = []
    
    # Fetch the top 5 recommended movies
    for i in distance[1:6]:
        movie_id = movies.iloc[i[0]]['id']  # Get the movie ID
        recommend_movie.append(movies.iloc[i[0]]['title'])  # Append movie title
        recommend_genre.append(movies.iloc[i[0]]['genre'])  # Append genre
        recommend_popularity.append(movies.iloc[i[0]]['popularity'])  # Append popularity score
        recommend_rating.append(movies.iloc[i[0]]['vote_average'])  # Append average rating
        recommend_releasedate.append(movies.iloc[i[0]]['release_date'])  # Append release date
        recommend_overview.append(movies.iloc[i[0]]['overview'])  # Append overview

        # Fetch and resize the poster image
        poster_url = fetch_poster(movie_id)
        if poster_url:
            recommend_poster.append(resize_image(poster_url))
        else:
            recommend_poster.append(None)  # Append None if no poster is found
    
    # Return all recommendation details
    return recommend_movie, recommend_rating, recommend_popularity, recommend_releasedate, recommend_overview, recommend_genre, recommend_poster

# Set the page layout to wide
st.set_page_config(layout="wide")

# Display the app header
st.header('Movie Recommender System')

# Dropdown for selecting a movie
selected_movie = st.selectbox('Select a movie', movies_list)

# When the "Recommend" button is clicked
if st.button('Recommend'):
    # Get the recommendation details for the selected movie
    movies_name, rating, popularity, release_date, overview, genre, movies_poster = recommend(selected_movie)
    
    # Display the recommendations in a vertical layout with three columns
    for i in range(len(movies_name)):
        col1, col2, col3 = st.columns(3, gap='medium')  # Divide the layout into three columns
        with col1:
            st.image(movies_poster[i])  # Display the movie poster in the first column
        with col2:
            st.header(f'**Title**:  {movies_name[i]}')  # Display the movie title
            st.markdown(f":star: {rating[i]} ({popularity[i]})")  # Display the rating and popularity
            st.subheader('**Description**')  # Subtitle for description
            st.text(overview[i])  # Display the movie overview
            st.subheader('**Genre**')  # Subtitle for genre
            st.text(genre[i])  # Display the movie genre
            st.text(release_date[i])  # Display the release date
        with col3:
            st.text('')  # Placeholder for additional content in the third column
