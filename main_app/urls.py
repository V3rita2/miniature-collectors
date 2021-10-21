from django.urls import path
from . import views

urlpatterns = [
    path('', views.Home.as_view(), name="home"),
    path('armies/', views.ArmiesList.as_view(), name="armies_list"),
    path('about/', views.About.as_view(), name='about'),
    path('armies/new/', views.ArmyCreate.as_view(), name='army_create'),
    path('army/<int:pk>/', views.ArmyDetail.as_view(), name="army_detail"),
    path('army/<int:pk>/update', views.ArmyUpdate.as_view(), name='army_update'),
    path('army/<int:pk>/delete', views.ArmyDelete.as_view(), name='army_delete'),
]