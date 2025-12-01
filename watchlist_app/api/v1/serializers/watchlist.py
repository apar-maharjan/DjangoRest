from rest_framework import serializers

from watchlist_app.models import Movie, Platform


# def length_validation(value):
#     if len(value) < 3:
#         raise serializers.ValidationError("The length of the movie must be at least 3 characters")
#     return value
#
#
# class WatchListSerializer(serializers.Serializer):
#     id = serializers.IntegerField( required = False)
#     name = serializers.CharField(validators=[length_validation])
#     description = serializers.CharField(validators=[length_validation])
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

    def validate_name(self, name):
        if len(name) > 10:
            raise serializers.ValidationError("Moive Name cannot be longer than 10 characters")
        return name

    def validate(self, data):
        if data['name'] == data['description']:
            raise serializers.ValidationError("Movie Name and Description Same Name")
        return data

class PlatformSerializer(serializers.ModelSerializer):
    class Meta:
        model = Platform
        fields = '__all__'