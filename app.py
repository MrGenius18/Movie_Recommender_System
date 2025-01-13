# streamlit run app.py

import streamlit as st
import pickle
import pandas as pd
import requests
import creds


movies_dict = pickle.load(open('movies_dict.pkl', 'rb'))
df = pd.DataFrame(movies_dict)

similarity = pickle.load(open('similarity.pkl', 'rb'))


def fetch_poster(movie_id):
    response = requests.get(f'https://api.themoviedb.org/3/movie/{movie_id}?{creds.api_key}')
    data = response.json()
    return "https://image.tmdb.org/t/p/w500/" + data['poster_path']

def recommend(movie):
    movie_index = df[df['title'] == movie].index[0]
    distances = similarity[movie_index]
    top5_movies_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]

    movies_name = []
    movies_poster = []
    for i in top5_movies_list:

        movies_name.append(df.iloc[i[0]].title)

        movie_id = df.iloc[i[0]].movie_id
        movies_poster.append(fetch_poster(movie_id))

    return movies_name, movies_poster


st.title('Movie Recommender System')

selected_movie_name = st.selectbox(
    "Select Your Movie Name", df['title'].values)

if st.button("Recommend"):
    names, posters = recommend(selected_movie_name)

    col1, col2, col3, col4, col5 = st.columns(5)

    with col1:
        st.text(names[0])
        st.image(posters[0])
    with col2:
        st.text(names[1])
        st.image(posters[1])
    with col3:
        st.text(names[2])
        st.image(posters[2])
    with col4:
        st.text(names[3])
        st.image(posters[3])
    with col5:
        st.text(names[4])
        st.image(posters[4])