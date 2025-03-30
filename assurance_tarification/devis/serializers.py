from rest_framework import serializers
from .models import Adresse, Devis

class AdresseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Adresse
        fields = ['numero', 'rue', 'code_postal', 'ville']

class DevisSerializer(serializers.ModelSerializer):
    adresse = AdresseSerializer()
    class Meta:
        model = Devis
        fields = ['id','num_opportunite', 'nom_client', 'tarif_propose', 'date_creation', 'description', 'type_garantie', 'type_bien', 'type_travaux', 'presence', 'client_vip', 'rcmo', 'taux_trc', 'taux_do', 'adresse']
        extra_kwargs = {
            'date_creation': {'read_only': True},  # Read-only, won't be used in POST/PUT
            'id': {'read_only': True}  # Read-only, won't be used in POST/PUT
        }

    def create(self, validated_data):
        print('validated_data : ', validated_data)
        adresse_data = validated_data.pop('adresse')
        adresse = Adresse.objects.create(**adresse_data)
        devis = Devis.objects.create(adresse=adresse, **validated_data)
        return devis