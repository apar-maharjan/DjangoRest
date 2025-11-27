from django.urls import path
from watchlist_app.api.v1.views.watchlist import movie_list, movie_details

app_name = 'watchlist_app'
urlpatterns =[
    path("list/", movie_list),
    path("<int:movie_id>/", movie_details)
]