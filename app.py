import streamlit as st
import pickle
import pandas as pd
import requests
import os
from dotenv import load_dotenv  # ✅ Load API Key securely

# ✅ Load environment variables from .env
load_dotenv()
TMDB_API_KEY = os.getenv("TMDB_API_KEY")  # Securely fetch API key

# ✅ Function to Fetch Movie Poster
def fetch_poster(movie_id):
    url = f"https://api.themoviedb.org/3/movie/{movie_id}?api_key={TMDB_API_KEY}&language=en-US"
    
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        if "poster_path" in data and data["poster_path"]:
            return f"https://image.tmdb.org/t/p/w500{data['poster_path']}"

    return "https://via.placeholder.com/150"  # Placeholder image if poster not found

# ✅ Movie Recommendation Function
def recommend(movie):
    movie_index = movies[movies['title'] == movie].index[0]  
    distances = similarity[movie_index]
    movies_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]  

    recommended_movies = []
    recommended_movies_poster = []
    
    for i in movies_list:
        movie_id = movies.iloc[i[0]].movie_id  # ✅ Get correct movie ID
        
        recommended_movies.append(movies.iloc[i[0]].title)
        recommended_movies_poster.append(fetch_poster(movie_id))  # ✅ Fetch poster securely
    
    return recommended_movies, recommended_movies_poster

# ✅ Load Movie Data & Similarity Matrix
movies_dict = pickle.load(open("model/movie_dict.pkl", "rb"))
movies = pd.DataFrame(movies_dict)
similarity = pickle.load(open("model/similarity.pkl", "rb"))

# ✅ Streamlit UI
st.title("🎬 Movie Recommender System")

selected_movie_name = st.selectbox(
    "Select a movie to get recommendations:",
    movies["title"].values  # ✅ Use movie titles
)

if st.button("Recommend"):
    names, posters = recommend(selected_movie_name)  # ✅ Fix unpacking

    # ✅ Display movie recommendations
    cols = st.columns(5)  # Create 5 columns
    
    for i in range(len(names)):
        with cols[i]:  # ✅ Arrange in columns
            st.image(posters[i], use_column_width=True, caption=names[i])
