from rest_framework import status, permissions
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from watchlist_app.api.v1.serializers.watchlist import WatchListSerializer, PlatformSerializer
from watchlist_app.models import Movie, Platform


# @api_view(['GET', 'POST'])
# def movie_list(request):
#     if request.method.lower() == 'get':
#         movies = Movie.objects.all()
#         serializer = WatchListSerializer(movies, many = True)
#         return Response(serializer.data)
#
#     if request.method.lower() == 'post':
#         serializer = WatchListSerializer(data = request.data)
#         serializer.is_valid(raise_exception = True)
#         serializer.save()
#         return Response(serializer.data)

class MovieListAPIView(APIView):
    def get(self, request):
        movies = Movie.objects.all()
        serializer = WatchListSerializer(movies, many=True, context = {"request": request})
        return Response(serializer.data)

    def post(self, request):
        serializer = WatchListSerializer(data = request.data, context = {"request": request})
        serializer.is_valid(raise_exception = True)
        serializer.save()
        return Response(serializer.data)

# @api_view(['GET', 'PUT','PATCH', 'DELETE'])
# def movie_details(request, movie_id):
#     if request.method.lower() == 'get':
#         movie = Movie.objects.get(id=movie_id)
#         serializer = WatchListSerializer(movie)
#         return Response(serializer.data)
#
#     if request.method.lower() == 'put':
#         movie = Movie.objects.get(id=movie_id)
#         serializer = WatchListSerializer(movie, data = request.data)
#         serializer.is_valid(raise_exception = True)
#         serializer.save()
#         return Response(serializer.data)
#
#     if request.method.lower() == 'delete':
#         movie = Movie.objects.get(id=movie_id)
#         movie.delete()
#         return Response({'message': 'Movie deleted'})
#
#     if request.method.lower() == 'patch':
#         movie = Movie.objects.get(id=movie_id)
#         serializer = WatchListSerializer(movie, data = request.data, partial = True)
#         serializer.is_valid(raise_exception = True)
#         serializer.save()
#         return Response(serializer.data)

class MovieDetailsAPIView(APIView):
    def get(self, request, movie_id):
        try:
            movie = Movie.objects.get(id = movie_id)
        except Movie.DoesNotExist:
            return Response({'message': 'Movie id does not exist'}, status.HTTP_404_NOT_FOUND)
        serializer = WatchListSerializer(movie, context = {"request": request})
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, movie_id):
        try:
            movie = Movie.objects.get(id = movie_id)
        except Movie.DoesNotExist:
            return Response({'message': 'Movie id does not exist'}, status.HTTP_404_NOT_FOUND)
        serializer = WatchListSerializer(movie, data = request.data, context={"request": request})
        serializer.is_valid(raise_exception = True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)

    def delete(self, request, movie_id):
        try:
            movie = Movie.objects.get(id = movie_id)
        except Movie.DoesNotExist:
            return Response({'message': 'Movie id does not exist'}, status.HTTP_404_NOT_FOUND)
        movie.delete()
        return Response({'message': 'Movie was deleted'}, status.HTTP_204_NO_CONTENT)

    def patch(self, request, movie_id):
        try:
            movie = Movie.objects.get(id = movie_id)
        except Movie.DoesNotExist:
            return Response({'message': 'Movie id does not exist'}, status.HTTP_404_NOT_FOUND)
        serializer = WatchListSerializer(movie, data = request.data, partial = True, context = {"request": request})
        serializer.is_valid(raise_exception = True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)


class PlatformListsAPIView(APIView):
    def get(self, request):
        platforms = Platform.objects.all()
        serializer = PlatformSerializer(platforms, many=True, context = {"request": request})
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = PlatformSerializer(data = request.data, context = {"request": request})
        serializer.is_valid(raise_exception = True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

class PlatformDetailAPIView(APIView):
    def get(self, request, platform_id):
            platform = Platform.objects.get(id = platform_id)
            serializer = PlatformSerializer(platform,context = {"request": request})
            return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, platform_id):
            platform = Platform.objects.get(id = platform_id)
            serializer = PlatformSerializer(platform, data = request.data, context = {"request": request})
            serializer.is_valid(raise_exception = True)
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)

    def delete(self, request, platform_id):
            platform = Platform.objects.get(id = platform_id)
            platform.delete()
            return Response({'message': 'Platform was deleted'}, status.HTTP_204_NO_CONTENT)

    def patch(self, request, platform_id):
        platform = Platform.objects.get(id = platform_id)
        serializer = PlatformSerializer(platform, data = request.data, partial = True, context = {"request": request})
        serializer.is_valid(raise_exception = True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)
