from django.urls import path
from . import views

urlpatterns = [
    path('', views.Home.as_view(), name="home"),
    path('armies/', views.ArmiesList.as_view(), name="armies_list")
]