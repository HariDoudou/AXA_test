from django.urls import path
from . import views

urlpatterns = [
    path('devis/', views.DevisList.as_view(), name='devis-list'),  # Pour récupérer la liste des devis
    path('devis/create/', views.DevisCreate.as_view(), name='devis-create'),  # Pour créer un nouveau devis
]
