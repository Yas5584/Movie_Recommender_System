from django.urls import path
from .views import get_recommendations,get_movie_poster

urlpatterns = [
    path('recommend/', get_recommendations),
    path('poster/', get_movie_poster)
]