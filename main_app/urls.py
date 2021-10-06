from django.urls import path
from . import views

urlpatterns = [
    path('', views.Home.as_view(), name="home"),
    path('gallery/', views.Gallery.as_view(), name="gallery")
]