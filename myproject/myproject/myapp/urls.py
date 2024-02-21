from django.urls import path
from . import views

urlpatterns = [
    path('profile/', views.profile_view, name='profile'),
    path('', views.index_view, name='index'),
    path('compare/', views.compare_view, name='compare'),
]
