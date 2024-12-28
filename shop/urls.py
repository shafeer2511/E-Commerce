from django.urls import path
from . import views  ## '.' means current project 
urlpatterns = [
    path('home',views.home,name="home")
]
