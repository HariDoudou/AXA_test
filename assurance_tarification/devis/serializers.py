from rest_framework import serializers
from .models import Devis

class DevisSerializer(serializers.ModelSerializer):
    class Meta:
        model = Devis
        fields = ['id', 'num_opportunite', 'nom_client', 'tarif_propose', 'date_creation']
