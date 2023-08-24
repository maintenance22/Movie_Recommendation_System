import pickle
import streamlit as st
import requests
import os 

# Set page configuration
st.set_page_config(
    page_title="Movie Recommender",
    page_icon="🎬",
    layout="wide",
    initial_sidebar_state="expanded",
)

def fetch_poster(movie_id):
    url = "https://api.themoviedb.org/3/movie/{}?api_key=8265bd1679663a7ea12ac168da84d2e8&language=en-US".format(movie_id)
    data = requests.get(url)
    data = data.json()
    poster_path = data['poster_path']
    full_path = "https://image.tmdb.org/t/p/w500/" + poster_path
    return full_path

def recommend(movie):
    index = movies[movies['title'] == movie].index[0]
    distances = sorted(list(enumerate(similarity[index])), reverse=True, key=lambda x: x[1])
    recommended_movie_names = []
    recommended_movie_posters = []
    for i in distances[1:6]:
        # fetch the movie poster
        movie_id = movies.iloc[i[0]].movie_id
        recommended_movie_posters.append(fetch_poster(movie_id))
        recommended_movie_names.append(movies.iloc[i[0]].title)

    return recommended_movie_names,recommended_movie_posters


# movies = pickle.load(open('model/movie_list.pkl','rb'))
# similarity = pickle.load(open('model/similarity.pkl','rb'))
script_directory = os.path.dirname(os.path.abspath(__file__))
movie_path = os.path.join(script_directory, 'model', 'movie_list.pkl')
similarity_path = os.path.join(script_directory, 'model', 'similarity.pkl')

# Load the pickle file
with open(movie_path, 'rb') as f:
    movies = pickle.load(f)

with open(similarity_path, 'rb') as f:
    similarity = pickle.load(f)
    

# App title and description
st.title('Movie Recommender System')
st.markdown("Select a movie from the dropdown and click the button to see recommendations")

# Movie selection dropdown
movie_list = movies['title'].values
selected_movie = st.selectbox("Select a Movie", movie_list)

# Recommendation button
if st.button('Show Recommendations'):
    recommended_movie_names, recommended_movie_posters = recommend(selected_movie)

    # col1, col2, col3, col4, col5 = st.beta_columns(5)
    col1, col2, col3, col4, col5 = st.columns(5)

    with col1:
        st.text(recommended_movie_names[0])
        st.image(recommended_movie_posters[0])
    with col2:
        st.text(recommended_movie_names[1])
        st.image(recommended_movie_posters[1])

    with col3:
        st.text(recommended_movie_names[2])
        st.image(recommended_movie_posters[2])
    with col4:
        st.text(recommended_movie_names[3])
        st.image(recommended_movie_posters[3])
    with col5:
        st.text(recommended_movie_names[4])
        st.image(recommended_movie_posters[4])
    
    # Add custom CSS styling

st.markdown(
    """
    <style>
    .reportview-container {
        background: url("https://i.ytimg.com/vi/S5c1ZhRdf1w/maxresdefault.jpg");
    }
   </style>
    """,
    unsafe_allow_html=True
)