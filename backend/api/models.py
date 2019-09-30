from django.db import models
from django.contrib.auth.models import User
# 평점 range 제한
from django.core.validators import MaxValueValidator, MinValueValidator

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    gender = models.CharField(max_length=10, default='M')
    age = models.IntegerField(default=25)
    occupation = models.CharField(max_length=200)
    group = models.IntegerField(default=0)
    description = models.CharField(max_length=200, default='')
    recommend_user = models.CharField(max_length=500)
    image = models.ImageField(blank=True)

#  wrapper for create user Profile
def create_profile(**kwargs):
    user = User.objects.create_user(
        username=kwargs['username'],
        password=kwargs['password'],
        is_active=True,
    )

    profile = Profile.objects.create(
        user=user,
        gender=kwargs['gender'],
        age=kwargs['age'],
        occupation=kwargs['occupation']
    )

    return profile

class Movie(models.Model):
    id = models.IntegerField(primary_key=True)
    title = models.CharField(max_length=200)
    genres = models.CharField(max_length=500)
    group = models.IntegerField(default=0)
    poster_url = models.TextField(default='')
    backdrop_url = models.TextField(default='')
    overview = models.TextField(default='')
    adult = models.BooleanField(default=False)
    recommend_movie = models.CharField(max_length=500)

    @property
    def genres_array(self):
        return self.genres.strip().split('|')

class Rating(models.Model):
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    rating = models.IntegerField(
        default=1,
        validators=[MaxValueValidator(5), MinValueValidator(1)]
    )
    rating_date = models.CharField(max_length=200)

class ClusterModel(models.Model):
    cluster_choice = models.BooleanField(default=True)
    based = models.CharField(max_length=30)
    method = models.IntegerField(
        default=1,
        validators=[MaxValueValidator(3), MinValueValidator(1)]
    )
    params = models.IntegerField(default=2)
