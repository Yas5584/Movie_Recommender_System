from rest_framework.decorators import api_view
from rest_framework.response import Response
from .engine import recommend_movie,fetch_poster
import requests

@api_view(['GET'])
def get_recommendations(request):
    movie = request.GET.get('movie')
    result = recommend_movie(movie)
    return Response({'recommendations': result})

# @api_view(['GET'])
# def get_movie_poster(request):
#     movie_id = request.GET.get('movie_id')
#     poster_url = fetch_poster(movie_id)
#     return Response({'poster_url': poster_url})

API_KEY = "e70c7205"

@api_view(['GET'])
def get_movie_poster(request):
    movie = request.GET.get('movie')

    if not movie:
        return Response({"error": "Movie not provided"}, status=400)

    # url = f"http://www.omdbapi.com/?t={movie}&apikey={API_KEY}"
    url = f"http://www.omdbapi.com/?t={movie}&type=movie&apikey={API_KEY}"
    res = requests.get(url)
    data = res.json()
    # print(data)

    return Response(data)
