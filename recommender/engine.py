import pandas as pd
import numpy as np
import pickle
import os
import requests
# BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
# # movies_list=pickle.load(open('movies.pkl','rb'))
# print(BASE_DIR)
# movies_list=pickle.load(open(os.path.join(BASE_DIR, 'data/movies.pkl'), 'rb'))

# # print(movies_list['title'].values)
# similarity_vectors=pickle.load(open(os.path.join(BASE_DIR, 'data/similarity_vectors.pkl'), 'rb'))

# print(similarity_vectors)



BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA_DIR = os.path.join(BASE_DIR, 'data')

os.makedirs(DATA_DIR, exist_ok=True)

def download_file(url, path):
    if not os.path.exists(path):
        print("Downloading:", path)
        r = requests.get(url)
        with open(path, 'wb') as f:
            f.write(r.content)


MOVIES_URL = "https://huggingface.co/datasets/YashEngineer/movie-recommender-data/resolve/main/movies.pkl"
SIMILARITY_URL = "https://huggingface.co/datasets/YashEngineer/movie-recommender-data/resolve/main/similarity_vectors.pkl"

movies_path = os.path.join(DATA_DIR, 'movies.pkl')
similarity_path = os.path.join(DATA_DIR, 'similarity_vectors.pkl')

download_file(MOVIES_URL, movies_path)
download_file(SIMILARITY_URL, similarity_path)



movies_list = pickle.load(open(movies_path, 'rb'))
similarity_vectors = pickle.load(open(similarity_path, 'rb'))
def recommend_movie(movie):
    list_movie=[]
    movie_index=movies_list[movies_list['title']==movie].index[0]
    distance=similarity_vectors[movie_index]
    movies=sorted(list(enumerate(distance)),reverse=True,key=lambda x:x[1])[1:6]
    # for i  in movie_list:
    #    return movies_list.iloc[i[0]].title
    for i in movies:
        list_movie.append(movies_list.iloc[i[0]].title)
    return list_movie
        
        # print(movies_list.iloc[i[0]].title)
        

def fetch_poster(movie_id):
    url = "https://www.omdbapi.com/?t={}&apikey=e70c7205".format(movie_id)
    data = requests.get(url)
    data = data.json()
    poster_path = data['Poster']
    full_path = poster_path
    return full_path



# print(recommend_movie('Avatar'))
