from rest_framework import status
from rest_framework.decorators import api_view
from api.models import Movie, Rating
from api.serializers import MovieSerializer
from rest_framework.response import Response


@api_view(['GET', 'POST', 'DELETE'])
def movies(request):

    if request.method == 'GET':
        id = request.GET.get('id', request.GET.get('movie_id', None))
        title = request.GET.get('title', None)
        genre = request.GET.get('genre', None)
        movies = Movie.objects.all()
        
        # profile에 있는 유저정보에서 나이, 성별, 직업을 가져오기
        age = request.GET.get('age', None)
        gender = request.GET.get('gender', None)
        occupation = request.GET.get('occupation', None)
        ratings = Rating.objects.all()

        if id:
            movies = movies.filter(pk=id)
        if title:
            movies = movies.filter(title__icontains=title)
        if genre:
            movies = movies.filter(genres__icontains=genre)
        # rating에서 user와 movie 오브젝트를 가져와서 리스트로 만든 후 중복제거 && id 순으로 정렬
        if age:
            movies = sorted(list(set([rate.movie for rate in ratings if (rate.user.profile.age == int(age))])), key=lambda x:x.id)
        if gender:
            movies = sorted(list(set([rate.movie for rate in ratings if (rate.user.profile.gender == gender)])), key=lambda x:x.id)
        if occupation:
            movies = sorted(list(set([rate.movie for rate in ratings if (rate.user.profile.occupation == occupation)])), key=lambda x:x.id)

        serializer = MovieSerializer(movies[:100], many=True)
        return Response(data=serializer.data, status=status.HTTP_200_OK)

    if request.method == 'DELETE':
        movie = Movie.objects.all()
        movie.delete()
        return Response(status=status.HTTP_200_OK)

    if request.method == 'POST':
        movies = request.data.get('movies', None)
        for movie in movies:
            id = movie.get('id', None)
            title = movie.get('title', None)
            genres = movie.get('genres', None)

            if not (id and title and genres):
                continue
            if Movie.objects.filter(id=id).count() > 0 or Movie.objects.filter(title=title).count() > 0:
                continue

            Movie(id=id, title=title, genres='|'.join(genres)).save()

        return Response(status=status.HTTP_200_OK)
