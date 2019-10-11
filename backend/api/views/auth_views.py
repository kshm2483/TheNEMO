from datetime import datetime, timedelta
from django.shortcuts import get_object_or_404, render
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from api.models import create_profile, Profile

# login에 필요한 것들 import
from django.contrib.auth import login, logout, authenticate
from api.serializers import UserSerializer, ProfileSerializer, ProfileUnRatedMovieSerializer
from django.contrib.auth.models import User
from django.contrib.sessions.models import Session

@api_view(['POST'])
def signup_many(request):
    if request.method == 'POST':
        profiles = request.data.get('profiles', None)
        for profile in profiles:
            username = profile.get('username', None)
            password = profile.get('password')
            age = profile.get('age', None)
            occupation = profile.get('occupation', None)
            gender = profile.get('gender', None)
            group = 1

            create_profile(username=username, password=password, age=age,
                            occupation=occupation, gender=gender, group=group)

        return Response(status=status.HTTP_201_CREATED)

@api_view(['POST'])
def signup(request):
    if request.method == 'POST':
        profiles = request.data.get('profiles', None)
        username = profiles.get('username', None)
        password = profiles.get('password')
        age = profiles.get('age', None)
        occupation = profiles.get('occupation', None)
        gender = profiles.get('gender', None)
        your_taste_movie = "1617|1646|1511|1547|798|888|1627|1401|849|1560|1513|834|851|1501|532|1590|542|1326|1598|1355|1098|19|1584|1596|1125|1526|1265|905|1173|1493|1567"

        create_profile(username=username, password=password, age=age,
                        occupation=occupation, gender=gender, your_taste_movie=your_taste_movie)

        return Response(status=status.HTTP_201_CREATED)

# 0828 / user login
@api_view(['POST'])
def userLogin(request):
    
    statCode = False
    serialData = { 'status': statCode, 'data': {}}
    # request payload에서 id, pw를 추출
    form = request.data
    id = form.get('username', None)
    pw = form.get('password', None)
    # DB에 있는 유저인지 확인, 존재하면 id를 user에 저장
    user = authenticate(username=id, password=pw)
    # user가 존재하고 is_active한지 check
    if user and user.is_active :
        statCode = True
        # DB에 login
        login(request, user=user)
        # user 정보를 같이 전달하기 위해서 req에서 받은 정보로 모델 가져오기
        user = User.objects.get(username=id)
        # serializer를 통해서 user, userprofile 정보를 함께 가져옴
        serializer = UserSerializer(user)
        serialData['status'] = statCode
        serialData['data'] = serializer.data
        profile = get_object_or_404(Profile, id=serializer.data['id'])
        serializer = ProfileSerializer(profile)
            
        if serializer.data['subscription_date'] :
            if round(datetime.now().timestamp()) > int(serializer.data['subscription_date']) + 2592000:
                profile.subscription = False
                profile = profile.save()  
                serialData['data'].update({'subscription':serializer.data['subscription']})
            else :
                now = round(datetime.now().timestamp()) - (int(serializer.data['subscription_date']))
                serialData['data'].update({'subscription':serializer.data['subscription'], 'remainingPeriod' : now})
        else:
            serialData['data'].update({'subscription':serializer.data['subscription']})
        return Response(data=serialData , status=status.HTTP_200_OK)
    # 실패시 빈값 return
    return Response(data=serialData, status=status.HTTP_200_OK)

# 0829 / logout
@api_view(['POST'])
def userLogout(request):
    logout(request)
    return Response(status=status.HTTP_200_OK)

@api_view(['GET', 'PATCH'])
def profile(request, user_id):
    if request.method == 'GET':
        profile = get_object_or_404(Profile, id=user_id)
        # profile = Profile.objects.get(id=user_id)
        serializer = ProfileSerializer(profile)
        return Response(data=serializer.data, status=status.HTTP_200_OK)

    if request.method == 'PATCH':
        profile = get_object_or_404(Profile, pk=user_id)
        # serializer = ProfileSerializer(profile)
        serializer = ProfileSerializer(profile, data=request.data, partial=True)
        if serializer.is_valid():
            profile = serializer.save()
            return Response(ProfileSerializer(profile).data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def profileSearch(request):
    if request.method == 'GET':
        username = request.GET.get('username')
        user = get_object_or_404(User, username=username)
        profile = get_object_or_404(Profile, id=user.id)
        serializer = ProfileSerializer(profile)
        return Response(data=serializer.data, status=status.HTTP_200_OK)

@api_view(['GET'])
def profileUnRatedMovieSearch(request, user_id):
    if request.method == 'GET':
        profile = get_object_or_404(Profile, id=user_id)
        serializer = ProfileUnRatedMovieSerializer(profile)
        return Response(data=serializer.data, status=status.HTTP_200_OK)


@api_view(['POST'])
def subscription(request, user_id):
    serialData = {'data': {}}
    if request.method == "POST":
        profile = get_object_or_404(Profile, id=user_id)
        profile.subscription = not profile.subscription
        if profile.subscription:
            profile.subscription_date = round(datetime.now().timestamp())
        profile = profile.save()
        user = User.objects.get(id=user_id)
        # serializer를 통해서 user, userprofile 정보를 함께 가져옴
        serializer = UserSerializer(user)

        serialData['data'] = serializer.data
        profile = get_object_or_404(Profile, id=serializer.data['id'])
        serializer = ProfileSerializer(profile)
        serialData['data'].update({'subscription':serializer.data['subscription']})
        return Response(data=serialData, status=status.HTTP_200_OK)
