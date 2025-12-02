from django.urls import path
from watchlist_app.api.v1.views.watchlist import MovieListAPIView, MovieDetailsAPIView, PlatformListsAPIView,PlatformDetailAPIView

app_name = 'watchlist_app'
urlpatterns =[
    path("list/", MovieListAPIView.as_view(), name="movie_lists"),
    path("<int:movie_id>/", MovieDetailsAPIView.as_view(), name="movie_details"),
    path("platform/", PlatformListsAPIView.as_view(), name="platform_lists"),
    path("platform/<int:platform_id>/", PlatformDetailAPIView.as_view(), name="platform_details"),

]