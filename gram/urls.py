from django.urls import path
from . import views

urlpatterns = [
    path('home/', views.main,name = 'home'),
    path('register/',views.register, name='register'),
    path('',views.loginuser,name='login_user')
]