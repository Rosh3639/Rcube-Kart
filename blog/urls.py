
from django.urls import path
from blog import views


urlpatterns = [
    path('', views.index, name='Home'),
    path('blogpost/<int:id>', views.blogpost, name='blogpost'),
]
