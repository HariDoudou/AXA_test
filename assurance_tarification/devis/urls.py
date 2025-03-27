from django.urls import path
from . import views

urlpatterns = [
    path('devis/', views.DevisAction.as_view(), name='devis-action'),
    path('devis/<int:id>/export/', views.DevisExport.as_view(), name='devis-export'),
]
