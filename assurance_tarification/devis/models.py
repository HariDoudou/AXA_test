from django.db import models

class Devis(models.Model):
    num_opportunite = models.CharField(max_length=50, unique=True)
    nom_client = models.CharField(max_length=255)
    tarif_propose = models.DecimalField(max_digits=10, decimal_places=2)
    date_creation = models.DateTimeField(auto_now_add=True)
    
    # On ajoutera plus tard des champs pour le fichier Word/PDF si nécessaire

    def __str__(self):
        return f"{self.num_opportunite} - {self.nom_client}"
