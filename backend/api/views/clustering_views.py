from django.http import JsonResponse
from django.contrib.auth.models import User
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from api.models import Movie, Rating, ClusterModel, Profile
from api.serializers import ClusterSerializer

from api.views.cluster_method.make_kmeans import kmeans_user, kmeans_movie
from api.views.cluster_method.KNN import knn_movie
from api.views.cluster_method.gmm import GaussianMix
from api.views.cluster_method.Hierarchical import Hierarchical
from api.views.recommend_method.matrix import MatrixFact
import pandas as pd
import numpy as np
from api.views.cluster_method.KNN import knn_user, knn_movie

@api_view(['POST'])
def setup(request):
    # 기본으로 설정되는 값은 kmeans, param=2
    # DB에 없으면 만든다.
    if not len(ClusterModel.objects.all()):
        ClusterModel.objects.create(based="user", method=1, params=2, id=1)
        user_result = kmeans_user(2, Movie.objects.all().values(), Rating.objects.all().values())
        for key, value in user_result.items():
            user = Profile.objects.get(id=key)
            user.group = value
            user.save()

        ClusterModel.objects.create(based="movie", method=1, params=2, id=2)
        movie_result = kmeans_movie(2, Movie.objects.all().values(), Rating.objects.all().values())
        for key, value in movie_result.items():
            movie = Movie.objects.get(id=key)
            movie.group = value
            movie.save()
    return Response(status=status.HTTP_200_OK)

# cluster model에서 user는 1번, movie는 2번
@api_view(['GET', 'POST'])
def cluster_user_method(request):

    if request.method == 'POST':
        method = request.data.get('method')
        params = request.data.get('params')
        if method:
            now = ClusterModel.objects.get(id=1)
            if params:
                params = int(params)
                algorithms = {'K':1, 'G':2, 'H':3}
                if method == 'K':
                    # kmeans algorithm 적용
                    result = kmeans_user(params, Movie.objects.all().values(), Rating.objects.all().values())
                if method == 'G':
                    # gausian algorithm 적용
                    gaussian = GaussianMix(Rating.objects.all().values(), Movie.objects.all().values(), 'user', params)
                    result = gaussian.get_result()

                if method == 'H':
                    # hierarchical algorithm 적용
                    hier = Hierarchical(Movie.objects.all().values(), Rating.objects.all().values(), 'user')
                    result = hier.cluster(params)
                for key, value in result.items():
                    user = Profile.objects.get(id=key)
                    user.group = value
                    user.save()
                now.method = algorithms[method]
                now.params = params
            
            else:
                if method == "knn":
                    result = knn_user(Movie.objects.all().values(), Rating.objects.all().values())[0]
                    # return 되는건 똑같으니까 똑같이 돌리면 됨
                
                    for key, value in result.items():
                        user = Profile.objects.get(id=key)
                        user.recommend_user = '|'.join(list(map(str, value)))
                        user.save()
                    now.cluster_choice = False

            # cluster method 저장
            now.save()
            return Response(status=status.HTTP_200_OK)
        return Response(status=status.HTTP_200_OK)

    if request.method == 'GET':
        now = ClusterModel.objects.get(id=1)
        serializer = ClusterSerializer(now)
        return Response(status=status.HTTP_200_OK)

@api_view(['GET', 'POST'])
def cluster_movie_method(request):
    if request.method == 'POST':
        method = request.data.get('method')
        params = request.data.get('params')

        if method:
            now = ClusterModel.objects.get(id=2)
            if params:
                params = int(params)
                if method == "K":
                    result = kmeans_movie(params, Movie.objects.all().values(), Rating.objects.all().values())

                if method == "G":
                    gaussian = GaussianMix(Rating.objects.all().values(), Movie.objects.all().values(), 'item', params)
                    result = gaussian.get_result()

                if method == 'H':
                    hier = Hierarchical(Movie.objects.all().values(), Rating.objects.all().values(), 'movie')
                    result = hier.cluster(params)
                
                for key, value in result.items():
                    movie = Movie.objects.get(id=key)
                    movie.group = value
                    movie.save()
                algorithms = {'K':1, 'G':2, 'H':3}
                now.method = algorithms[method]
                now.params = params
            else:
                if method == "knn":
                    print(2)
                    pass
                    result = knn_movie(Movie.objects.all().values(), Rating.objects.all().values())
                    # return 되는건 똑같으니까 똑같이 돌리면 됨
                    for key, value in result.items():
                        user = Movie.objects.get(id=key)
                        user.recommend_movie = '|'.join(list(map(str, value)))
                        user.save()
                    now.cluster_choice = False

            # cluster method 저장
            now.save()
            return Response(status=status.HTTP_200_OK)

    if request.method == 'GET':
        now = ClusterModel.objects.get(id=2)
        serializer = ClusterSerializer(now)
        return Response(data=serializer.data)

@api_view(['POST'])
def user_customized_recommendation(request):
    method = request.data.get('method')
    # matrix를 쓰는 경우
    if method == "matrix":
        movies = Movie.objects.all().values()
        ratings = Rating.objects.all().values()
        users = User.objects.all()
        factorizer = MatrixFact(movies, ratings, k=3, learning_rate=0.01, reg_param=0.01, epochs=300, verbose=True)
        result = [list(map(lambda x: round(float(x),2), res)) for res in factorizer.get_complete_matrix()]
        for i in range(len(result)):
            # 추천 영화의 id리스트
            top = []
            user_id = users[i+1].id
            profile = Profile.objects.get(id=user_id)
            rated_movie = [r.id for r in users.get(id=user_id).rating_set.all()]
            for val in sorted(result[i]):
                top += [j for j in range(len(result[i])) if val == result[i][j] and j not in rated_movie]
                if len(top) > 30:
                    break
            # 유저 번호 뽑기
            profile.your_taste_movie = '|'.join(list(map(str, top)))
            profile.save()
        return Response(status=status.HTTP_200_OK)
    
    if method == "knn":
        # knn 알고리즘 구현이 필요
        result = knn_user(Movie.objects.all().values(), Rating.objects.all().values())[1]
        for key, value in result.items():
            user = Profile.objects.get(id=key)
            user.your_taste_movie = '|'.join(list(map(str, value)))
            user.save()
        return Response(status=status.HTTP_200_OK)

