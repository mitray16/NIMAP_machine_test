from django.urls import path
from .views import (
    ClientListCreateView,
    ClientRetrieveUpdateDestroyView,
    ProjectCreateView,
    UserProjectsListView,
)

urlpatterns = [
    path('clients/', ClientListCreateView.as_view(), name='client-list-create'),
    path('clients/<int:pk>/', ClientRetrieveUpdateDestroyView.as_view(), name='client-detail'),
    path('clients/<int:client_id>/projects/', ProjectCreateView.as_view(), name='project-create'),
    path('projects/', UserProjectsListView.as_view(), name='user-projects'),
]
