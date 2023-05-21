import pickle
import streamlit as st
import requests
import pandas as pd
from PIL import Image

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
    for i in distances[1:7]:
        # fetch the movie poster
        movie_id = movies.iloc[i[0]].movie_id
        recommended_movie_posters.append(fetch_poster(movie_id))
        recommended_movie_names.append(movies.iloc[i[0]].title)

    return recommended_movie_names,recommended_movie_posters


# st.header('Movie Recommender System')
import streamlit as st
st.markdown("<h1 style='text-align: center;'>Movie Recommender System</h1>", unsafe_allow_html=True)

movies = pd.read_pickle('model/movie_list.pkl')
similarity = pd.read_pickle('model/similarity.pkl')

movie_list = movies['title'].values
selected_movie = st.selectbox(
    "Type or select a movie from the dropdown",
    movie_list
)


if st.button('Show Recommendation'):
    st.divider()

    recommended_movie_names,recommended_movie_posters = recommend(selected_movie)
    
    col1, col2 = st.columns(2)
    with col1:
        # st.text(recommended_movie_names[0])
        st.image(recommended_movie_posters[0],caption=recommended_movie_names[0],use_column_width=True)
        
    with col2:
        # st.text(recommended_movie_names[1])
        st.image(recommended_movie_posters[1],caption=recommended_movie_names[1],use_column_width=True)

    col3,col4 = st.columns(2)
    with col3:
        # st.text(recommended_movie_names[2])
        st.image(recommended_movie_posters[2],caption=recommended_movie_names[2],use_column_width=True)
    
    with col4:
        # st.text(recommended_movie_names[3])
        st.image(recommended_movie_posters[3],caption=recommended_movie_names[3],use_column_width=True)

    col5,col6 = st.columns(2)
    with col5:
        # st.text(recommended_movie_names[4])
        st.image(recommended_movie_posters[4],caption=recommended_movie_names[4],use_column_width=True)
    with col6:
        # st.text(recommended_movie_names[5])
        st.image(recommended_movie_posters[5],caption=recommended_movie_names[5],use_column_width=True)


st.divider() 
col1, col2 = st.columns(2)
col1.markdown(" By :- Himanshu Bag")
col2.markdown(" Github Link for this project : [Click-Me](https://github.com/0x1h0b/Emotion-from-Text)")
col1, col2 = st.columns(2)
col1.markdown(" LinkedIn Profile : [himanshu-bag](https://www.linkedin.com/in/himanshu-bag/)")
col2.markdown(" Github Profile : [0x1h0b](https://github.com/0x1h0b)")
st.divider()



