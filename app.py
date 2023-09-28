import streamlit as st
import pickle
import pandas as pd
import requests


#https://docs.streamlit.io/library/api-reference/layout/st.columns
# load_dotenv()
# def fetch_poster(movie_id):
#     response = requests.get("https://api.themoviedb.org/3/keyword/{}?api_key={}/movies?include_adult=false&language=en-US&page=1".format(movie_id,os.getenv('API_KEY')))
#     # headers = {"accept": "application/json"}
#     # response = requests.get(url, headers=headers)
#     data = response.json()
#     print(data)
#     return "https://image.tmdb.org/t/p/w500" + data['poster_path']

def recommend(movie):
    movie_index = movies[movies['title'] == movie].index[0]
    distances = similarity[movie_index]
    movies_list = sorted(list(enumerate(distances)),reverse=True,key = lambda x:x[1])[1:6]
    
    recommended_movies = []
    # recommended_movies_posters = []
    
    for i in movies_list:
        # movie_id = movies.iloc[i[0]].movie_id
        recommended_movies.append(movies.iloc[i[0]].title)
        # fetch poster from api
        # recommended_movies_posters.append(fetch_poster(i[0]))
    return recommended_movies

movies_dict = pickle.load(open('movie_dict.pkl','rb'))
movies = pd.DataFrame(movies_dict)
# movies_list = movies_list['title'].values
# st.title('Movie Recommender System')
selected_movie_name = st.selectbox(
    'What movie did you watch?',
    movies['title'].values)
similarity =  pickle.load(open('similarity.pkl','rb'))
# st.write('You selected:', option)

# if st.button('Recommend'):
#     names, posters = recommend(selected_movie_name)
#     # col1, col2, col3,col4,col5 = st.columns(5)
#     # with col1:
#     #     st.header(names[0])
#     #     st.image(posters[0])

#     # with col2:
#     #     st.header(names[1])
#     #     st.image(posters[1])

#     # with col3:
#     #     st.header(names[2])
#     #     st.image(posters[2])
        
#     # with col4:
#     #     st.header(names[4])
#     #     st.image(posters[4])

#     # with col5:
#     #     st.header(names[5])
#     #     st.image(posters[5])
#     for i in range(len(names)):
#         col1, col2, col3,col4,col5 = st.columns(5)
#         with col1:
#             st.header(names[i])
#             st.image(posters[i])
if st.button('Recommend'):
    recommendations = recommend(selected_movie_name)
    for i in recommendations:
        st.write(i)
        
        
        

