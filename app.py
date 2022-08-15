import streamlit as st
import pickle
import requests


def fetch_poster(movie_id):
     url = "https://api.themoviedb.org/3/movie/{}?api_key=b460a03cfce416500eaf3670a590839a&language=en-US".format(movie_id)
     data = requests.get(url)
     data = data.json()
     poster_path = data['poster_path']
     full_path = "https://image.tmdb.org/t/p/w500/" + poster_path
     return full_path


def recommend(movie):
     movie_index = movies_list[movies_list['title'] == movie].index[0]
     distance = sorted(list(enumerate(similarity[movie_index])), reverse=True, key=lambda x: x[1])
     recommended_movie_names = []
     recommended_movie_posters = []

     for i in distance[1:6]:
          # fetching poster
          movie_id = movies_list.iloc[i[0]].movie_id
          recommended_movie_posters.append(fetch_poster(movie_id))

          # recommended movie list
          recommended_movie_names.append(movies_list.iloc[i[0]].title)
     return  recommended_movie_names, recommended_movie_posters




st.header('Movie Recommender System')
movies_list = pickle.load(open('movies.pkl','rb'))
similarity = pickle.load(open('similarity.pkl','rb'))

movies = movies_list['title'].values
selected_movie= st.selectbox(
     'Type or select a movie from the dropdown',
     movies)

if st.button('Show Recommend'):
     recommended_movie_names, recommended_movie_posters = recommend(selected_movie)

     col1, col2, col3, col4, col5 = st.columns(5)
     with col1:
          st.image(recommended_movie_posters[0])
          st.text(recommended_movie_names[0])

     with col2:
          st.image(recommended_movie_posters[1])
          st.text(recommended_movie_names[1])

     with col3:
          st.image(recommended_movie_posters[2])
          st.text(recommended_movie_names[2])

     with col4:
          st.image(recommended_movie_posters[3])
          st.text(recommended_movie_names[3])

     with col5:
          st.image(recommended_movie_posters[4])
          st.text(recommended_movie_names[4])
