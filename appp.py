import streamlit as st
import pickle
import requests


movies = pickle.load(open("C:\\Users\\DELL\\Desktop\\bharath_intern\\movie recommendation\\movies_list.pkl", 'rb'))
similarity = pickle.load(open("C:\\Users\\DELL\\Desktop\\bharath_intern\\movie recommendation\\similarity.pkl", 'rb'))
movies_list = movies['title'].values

st.header("Movie Recommendation System")

# Create a dropdown to select a movie
selected_movie = st.selectbox("Select a movie:", movies_list)

import streamlit.components.v1 as components

def recommend(movie):
    index = movies[movies['title'] == movie].index[0]
    distance = sorted(list(enumerate(similarity[index])), reverse=True, key=lambda vector: vector[1])
    recommend_movie = []
    for i in distance[1:6]:
        movies_id = movies.iloc[i[0]].id
        recommend_movie.append(movies.iloc[i[0]].title)
    return recommend_movie

if st.button("Recommend"):
    movie_name = recommend(selected_movie)
    col1, col2, col3, col4, col5 = st.columns(5)
    with col1:
        st.text(movie_name[0])
    with col2:
        st.text(movie_name[1])
    with col3:
        st.text(movie_name[2])
    with col4:
        st.text(movie_name[3])
    with col5:
        st.text(movie_name[4])

