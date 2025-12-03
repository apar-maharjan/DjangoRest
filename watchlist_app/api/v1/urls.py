from django.urls import path
from watchlist_app.api.v1.views.watchlist import MovieListAPIView, MovieDetailsAPIView, PlatformListsAPIView, \
    PlatformDetailAPIView, ReviewListAPIView, ReviewDetailAPIView

app_name = 'watchlist_app'
urlpatterns =[
    path("list/", MovieListAPIView.as_view(), name="movie_list"),
    path("<int:movie_id>/", MovieDetailsAPIView.as_view(), name="movie_detail"),
    path("platform/", PlatformListsAPIView.as_view(), name="platform_list"),
    path("platform/<int:platform_id>/", PlatformDetailAPIView.as_view(), name="platform_detail"),
    path("review/", ReviewListAPIView.as_view(), name="review_list"),
    path("review/<int:pk>/", ReviewDetailAPIView.as_view(), name="review_detail"),
]