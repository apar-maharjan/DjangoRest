from django.shortcuts import render
from  django.http import JsonResponse
from rest_framework.response import Response
from rest_framework.decorators import api_view
from watchlist_app.api.v1.serializers.watchlist import WatchListSerializer
from watchlist_app.models import Movie

@api_view(['GET', 'POST'])
def movie_list(request):
    if request.method.lower() == 'get':
        movies = Movie.objects.all()
        serializer = WatchListSerializer(movies, many = True)
        return Response(serializer.data)

    if request.method.lower() == 'post':
        serializer = WatchListSerializer(data = request.data)
        serializer.is_valid(raise_exception = True)
        serializer.save()
        return Response(serializer.data)

@api_view(['GET', 'PUT','PATCH', 'DELETE'])
def movie_details(request, movie_id):
    if request.method.lower() == 'get':
        movie = Movie.objects.get(id=movie_id)
        serializer = WatchListSerializer(movie)
        return Response(serializer.data)

    if request.method.lower() == 'put':
        movie = Movie.objects.get(id=movie_id)
        serializer = WatchListSerializer(movie, data = request.data)
        serializer.is_valid(raise_exception = True)
        serializer.save()
        return Response(serializer.data)

    if request.method.lower() == 'delete':
        movie = Movie.objects.get(id=movie_id)
        movie.delete()
        return Response({'message': 'Movie deleted'})

    if request.method.lower() == 'patch':
        movie = Movie.objects.get(id=movie_id)
        serializer = WatchListSerializer(movie, data = request.data, partial = True)
        serializer.is_valid(raise_exception = True)
        serializer.save()
        return Response(serializer.data)