from django.urls import path
from .views import get_counties, get_districts,get_school_names
from .views import get_school_names_by_type
from .views import school_data_endpoint

from . import views


urlpatterns = [
    path('profile/', views.profile_view, name='profile'),
    path('', views.index_view, name='index'),
    path('compare/', views.compare_view, name='compare'),
    path('data/', views.display_table1_data, name='display_table1_data'),
    path('examp/', views.display_pssa_exam_data, name='display_pssa_exam_data'),
    path('keystone/', views.display_keystone_exam_data, name='display_keystone_exam_data'),
    path('district/', views.display_district_data, name='display_district_data'),
    path('view_data/', views.view_data, name='view_data'),
    path('get-counties/', get_counties, name='get-counties'),
    path('get-districts/<str:county_name>/', get_districts, name='get-districts'),
    path('get-school-ids/<str:school_type>/', views.get_school_ids, name='get_school_ids'),
    path('get-school-names/<str:school_type>/', get_school_names, name='get-school-names'),
    path('school-data/<int:school_number>/', school_data_endpoint, name='school-data-endpoint'),
    path('get-school-names-by-type/<str:school_type>/', get_school_names_by_type, name='get-school-names-by-type'),
]
