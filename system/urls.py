from django.urls import path
from . import views


urlpatterns = [    
               path('', views.index, name='index'),
               path('recommend/', views.recommend, name='recommend'),
               path('about/', views.about, name='about'),
]