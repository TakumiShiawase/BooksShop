from django.urls import path
from . import views
urlpatterns = [
    path('signup', views.signup, name='signup'),
    path('signin', views.signin, name='signin'),
    path('settings', views.settings, name='settings'),
    path('follow', views.follow, name='follow'),
    path('logout', views.logout, name='logout'),
    path('profile/<str:pk>', views.profile, name='profile'),
    ]