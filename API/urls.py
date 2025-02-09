
from .views import index,login_user
from django.urls import path


urlpatterns = [
    path('protected-route/', index,name='index'),
    path('login_user/',login_user, name='login_user'),
]
