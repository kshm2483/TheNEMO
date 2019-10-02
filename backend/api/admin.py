from django.contrib import admin
from .models import Profile, Movie, Rating, ClusterModel

# Register your models here.
# class MovieAdmin(admin.ModelAdmin):
#     fields = ['id', 'title', 'genres', 'group', 'poster_url']

class RatingAdmin(admin.ModelAdmin):
    fields = ['user', 'movie','rating_date','rating']

admin.site.register(Profile)
admin.site.register(Movie)
# admin.site.register(Movie, MovieAdmin)
admin.site.register(Rating, RatingAdmin)
admin.site.register(ClusterModel)