from django.urls import path
from .views import CreateReclamationView,ReclamationDelete, ReclamationListView
urlpatterns = [
    path('reclamations/', CreateReclamationView.as_view(), name='reclamation_list_create'),  
    path('reclamations/list/', ReclamationListView.as_view(), name='list-reclamation'),
    path('reclamations/delete/<int:pk>/', ReclamationDelete.as_view(), name='reclamation_delete'),
]


