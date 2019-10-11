from datetime import datetime
from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.decorators import api_view
from api.models import Rating, Movie, User
from api.serializers import RatingSerializer
from rest_framework.response import Response

@api_view(['POST'])
def rating_many(request):
    if request.method == 'POST':
        ratings = request.data.get('ratings', None)

        for rate in ratings:
            userid = rate.get('userid', None)
            movieid = rate.get('movieid', None)
            rating = rate.get('rating', None)
            timestamp = rate.get('timestamp', None)
            
            Rating(movie_id=movieid, user_id=userid, rating=rating, rating_date=timestamp).save()

        return Response(status=status.HTTP_200_OK)

@api_view(['POST', 'PATCH'])
def rating(request):
    
    if request.method == "POST":
        user = request.data['user']
        movie = request.data['movie']
        if Rating.objects.filter(user=user, movie=movie):
            return Response(status=status.HTTP_400_BAD_REQUEST)
        else :
            serializer = RatingSerializer(data=request.data)
            if serializer.is_valid():
                rating = serializer.save(user=User.objects.get(id=user), movie=Movie.objects.get(id=movie), rating_date = round(datetime.now().timestamp()))
                return Response(RatingSerializer(rating).data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    if request.method == "PATCH":
        user = request.data.get('user')
        movie = request.data.get('movie')
        if Rating.objects.filter(user=user, movie=movie):
            rating = get_object_or_404(Rating, user=user, movie=movie)
            serializer = RatingSerializer(rating, data=request.data, partial=True)
            if serializer.is_valid():
                rating = serializer.save(rating_date = round(datetime.now().timestamp()))
                return Response(RatingSerializer(rating).data)
        else :
            serializer = RatingSerializer(data=request.data)
            if serializer.is_valid():
                rating = serializer.save(user=User.objects.get(id=user), movie=Movie.objects.get(id=movie), rating_date = round(datetime.now().timestamp()))
                return Response(RatingSerializer(rating).data, status=status.HTTP_201_CREATED)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


    #     rating = request.data.get('rating')
    #     userid = rating.get('userid')
    #     movieid = rating.get('movieid')
    #     rate_value = rating.get('rate')
    #     timestamp = round(datetime.now().timestamp())
    #     Rating(movie_id=movieid, user_id=userid, rating=rate_value, rating_date=timestamp).save()

    # return Response(status=status.HTTP_200_OK)
