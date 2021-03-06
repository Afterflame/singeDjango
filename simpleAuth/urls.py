from django.contrib.auth import views as auth_views
from . import views
from django.conf.urls import url
from django.urls import path

urlpatterns = [
    path('login/', auth_views.LoginView.as_view(), {'template_name':'../simpleAuth/login.html'}, name='login'),
    path('logout/', views.loglogout),
    path('registration/', views.registration),
]