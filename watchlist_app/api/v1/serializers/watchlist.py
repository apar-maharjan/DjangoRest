from rest_framework import serializers

from watchlist_app.models import Movie


# class WatchListSerializer(serializers.Serializer):
#     id = serializers.IntegerField()
#     name = serializers.CharField()
#     description = serializers.CharField()
#     active = serializers.BooleanField()
#
#     def create(self, validated_data):
#         movie =Movie.objects.create(name = validated_data['name'], description = validated_data['description'], active = validated_data['active'])
#         return movie
#
#     def update(self, instance, validated_data):
#         instance.name = validated_data.get('name', instance.name)
#         instance.description = validated_data.get('description', instance.description)
#         instance.active = validated_data.get('active', instance.active)
#         instance.save()
#         return instance

class WatchListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = '__all__'