from django.urls import path
from . import views


urlpatterns = [
    path('', views.ProyectView.as_view(), name='home'),
    path('springs/<int:pk_proyect>/', views.SpringsView.as_view(), name='springs-list'),
    path('proyect-create/', views.ProyectCreateView.as_view(), name='proyect-create'),

    # Activities
    path('<int:pk_spring>/', views.ActivitiesListView.as_view(), name='activities'),
    path('create/<int:spring>/', views.ActivityCreateView.as_view(), name='activity-create'),
]
