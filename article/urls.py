from django.urls import path
from . import views

app_name = 'article'
urlpatterns = [
    path('', views.index, name='index'),
    path('learn/', views.learn, name='learn'),
    path('about/', views.about, name='about'),
]