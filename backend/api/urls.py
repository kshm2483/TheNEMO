from django.conf.urls import url
from django.urls import path
from api.views import movie_views, rating_views, auth_views, clustering_views

urlpatterns = [
    # 초기 setup을 위한 url
    url('auth/signup-many/$', auth_views.signup_many, name='sign_up_many'),
    url('auth/signup/$', auth_views.signup, name='sign_up'),
    url('rating_many/$', rating_views.rating_many, name='rating_list'),
    url('cluster/', clustering_views.setup, name="cluster_setup"),

    url('movies/$', movie_views.movies, name='movie_list'),
    
    url('rating/$', rating_views.rating, name='rating'),

    path('profile/<int:user_id>', auth_views.profile, name='profile'),
    url('auth/login', auth_views.userLogin, name='login'),
    url('auth/logout', auth_views.userLogout, name='logout'),

    url('cluster/user', clustering_views.cluster_user_method, name="cluster_user_method"),
    url('cluster/movie', clustering_views.cluster_movie_method, name="cluster_movie_method"),

    path('subscription/<int:user_id>', auth_views.subscription, name="subscription"),
]