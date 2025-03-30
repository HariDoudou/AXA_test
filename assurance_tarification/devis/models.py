from django.db import models



class Adresse(models.Model):
    numero = models.CharField(max_length=10, null=True)
    rue = models.CharField(max_length=255, null=True)
    code_postal = models.CharField(max_length=10, null=True)
    ville = models.CharField(max_length=100, null=True)

    def __str__(self):
        return f"{self.numero} {self.rue}, {self.code_postal} {self.ville}"
    

class Devis(models.Model):
    num_opportunite = models.CharField(max_length=50, unique=True)
    nom_client = models.CharField(max_length=255)
    tarif_propose = models.DecimalField(max_digits=10, decimal_places=2, default=0.0)
    date_creation = models.DateTimeField(auto_now_add=True)
    description = models.TextField(null=True)
    type_garantie = models.CharField(max_length=50, null=True)
    type_bien = models.CharField(max_length=50, null=True)
    type_travaux = models.CharField(max_length=50, null=True)
    presence = models.BooleanField(default=False)
    client_vip = models.BooleanField(default=False)
    rcmo = models.BooleanField(default=False)
    taux_trc = models.DecimalField(max_digits=10, decimal_places=2, default=0.0)
    taux_do = models.DecimalField(max_digits=10, decimal_places=2, default=0.0)
    # On ajoute un champ pour l'adresse du client
    adresse = models.ForeignKey(Adresse, on_delete=models.CASCADE, null=True)

    @property
    def tarif_trc(self):
        if self.tarif_propose is None  or self.taux_trc is None:
            return 0
        return self.taux_trc * self.tarif_propose
    
    @property
    def tarif_do(self):
        if self.tarif_propose is None or self.taux_do is None:
            return 0
        return self.taux_do * self.tarif_propose
    
    @property
    def tarif_duo(self):
        return self.tarif_do + self.tarif_trc
    
    @property
    def prime_total(self):
        if(self.type_garantie == 'TRC'):
            return self.tarif_trc
        elif(self.type_garantie == 'DO'):
            return self.tarif_do
        else:
            return self.tarif_duo
    