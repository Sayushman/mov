import streamlit as st
import pickle
import pandas as pd
import requests

def fetch_poster(movie_id):
    response = requests.get('https://api.themoviedb.org/3/movie/{}?api_key=749c95792aa3e0373acfad3ddc8aa882&language=en-US'.format(movie_id))
    data = response.json()
    return "https://image.tmdb.org/t/p/original" + data['poster_path']

def recommend(movie):
    # def recommend(movies):
    movie_index = movies[movies['title'] == movie].index[0]
    distances = similarity[movie_index]
    movies_list = sorted(list(enumerate(distances)),reverse=True,key=lambda x:x[1])[1:6]

    recommend_movies = []
    recommended_movies_posters = []
    for i in movies_list:
        movie_id = movies.iloc[i[0]].movie_id
        # fetch name
        recommend_movies.append(movies.iloc[i[0]].title)
        # fetch poster from api
        recommended_movies_posters.append(fetch_poster(movie_id))
    return recommend_movies,recommended_movies_posters
    # return recommend_movies


movies_dict = pickle.load(open('/home/aayu/Documents/PROJECTS/MovRECcom/movies_dict.pkl','rb'))
movies = pd.DataFrame(movies_dict)

similarity = pickle.load(open('/home/aayu/Documents/PROJECTS/MovRECcom/similarity.pkl','rb'))

st.title('Movie Recommender System')

selected_movie_name = st.selectbox(
    'Choose the type of movie you want to get recommended for: ',
    movies['title'].values)

st.write('You selected:', selected_movie_name)


st.button("Reset", type="primary")
if st.button('Recommend'):
    # recommendations = recommend(selected_movie_name)
    names,posters = recommend(selected_movie_name)
    
    col1, col2, col3, col4, col5 = st.beta_columns(5)
    with col1:
        st.header(names[0])
        st.image(posters[0])
    # api_tmdbAPI-::749c95792aa3e0373acfad3ddc8aa882
    with col2:
        st.header(names[1])
        st.image(posters[1])
    # api_tmdbAPI-::749c95792aa3e0373acfad3ddc8aa882
    with col3:
        st.header(names[2])
        st.image(posters[2])
    with col4:
        st.header(names[3])
        st.image(posters[3])
    with col5:
        st.header(names[4])
        st.image(posters[4])
    # api_tmdbAPI-::749c95792aa3e0373acfad3ddc8aa882