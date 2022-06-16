from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('home/', views.index, name='home'),
    path('signup/', views.sign_up, name='signup'),
    path('profile/', views.profile, name='profile'),
    path('editprofile/', views.editprofile, name='editprofile'),
    path('areahood/', views.areahood, name='areahood'),
    path('business/', views.business, name='business'),
]