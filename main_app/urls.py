from django.urls import path
from . import views

urlpatterns = [
    path('', views.Home.as_view(), name="home"),
    path('armies/', views.ArmiesList.as_view(), name="armies_list"),
    path('about/', views.About.as_view(), name='about'),
    path('armies/new/', views.ArmyCreate.as_view(), name='army_create')
]