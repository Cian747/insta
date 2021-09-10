from django.urls import path
from . import views

urlpatterns = [
    path('home/', views.main,name = 'index'),
    path('register/',views.register_user, name='register'),
    path('',views.login_user,name='login_user')
]