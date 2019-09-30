from django.db.models import Avg
from rest_framework import serializers
from .models import Profile, Movie, Rating, ClusterModel
from django.contrib.auth.models import User

class ProfileSerializer(serializers.ModelSerializer):
    id = serializers.ReadOnlyField()
    username = serializers.SerializerMethodField('get_username')
    is_staff = serializers.SerializerMethodField('get_is_staff')
    similaruser = serializers.SerializerMethodField('get_group')
    ratingmovie = serializers.SerializerMethodField('get_ratingmovie')
    image = serializers.ImageField(use_url=True)

    class Meta:
        model = Profile
        fields = ('id', 'username', 'is_staff', 'gender', 'age', 'occupation', 'group', 'similaruser', 'ratingmovie', 'image')

    def get_username(self, obj):
        return obj.user.username
    
    def get_ratingmovie(self, obj):
        data = User.objects.get(id=obj.id)
        return [data.movie.title for data in data.rating_set.all()]

    def get_is_staff(self, obj):
        return obj.user.is_staff
        
    def get_group(self, obj):
        if ClusterModel.objects.get(id=1).cluster_choice:
            users = Profile.objects.filter(group=obj.user.profile.group)
            data = [i.id for i in users]
        else:
            data = obj.recommend_user.split('|')
            return data


class RatingSerializer(serializers.ModelSerializer):
    # user = serializers.SerializerMethodField('get_profileInfo')
    
    class Meta:
        model = Rating
        fields = [ 'rating', 'rating_date',]

    # def get_profileInfo(self, obj):
    #     return { 'id':obj.user.id, 'name': obj.user.username, 'Gender': obj.user.profile.gender, 'age': obj.user.profile.age, 'Occupation': obj.user.profile.occupation }

class MovieSerializer(serializers.ModelSerializer):
    genres_array = serializers.ReadOnlyField()
    rating = RatingSerializer(many=True, read_only=True, source='rating_set')
    view_cnt = serializers.ReadOnlyField(source='rating_set.count')
    average_rating = serializers.SerializerMethodField()
    similarmovie = serializers.SerializerMethodField('get_group')

    class Meta:
        model = Movie
        fields = ['id', 'title', 'genres_array', 'view_cnt', 'rating', 'average_rating', 'group', 'similarmovie', 'poster_url', 'backdrop_url', 'overview', 'adult']

    def get_average_rating(self, obj):
        average = obj.rating_set.all().aggregate(Avg('rating')).get('rating__avg')
        if average is None:
            return 0
        else:
            return round(average, 1)

    def get_group(self, obj):
        # 2번이 영화니까
        if ClusterModel.objects.get(id=2).cluster_choice:
            movies = Movie.objects.filter(group=obj.group)
            recommendation_movies = [i.pk for i in movies]
        else:
            # 3주차 recommendation 저장된 리스트 보내주기
            recommendation_movies = obj.recommend_movie.split('|')
        return recommendation_movies

class UserSerializer(serializers.ModelSerializer):
    profile = serializers.SerializerMethodField('get_profileInfo')
    class Meta:
        model = User
        fields = ('id', 'username', 'is_staff', 'profile')
        
    def get_profileInfo(self, obj):
        return { 'gender': obj.profile.gender, 'age': obj.profile.age, 'Occupation': obj.profile.occupation }

class ClusterSerializer(serializers.ModelSerializer):
    class Meta:
        model = ClusterModel
        fields = ('id', 'cluster_choice', 'based', 'method', 'params')