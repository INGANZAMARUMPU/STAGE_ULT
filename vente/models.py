from django.db import models
from django.contrib.auth.models import User

class Produit(models.Model):
    id = models.AutoField(primary_key=True)
    nom = models.CharField(max_length=31)
    unite = models.CharField(max_length=31)
    quantinte = models.FloatField(editable=False, null=True)
    prix = models.FloatField()

    def __str__(self):
        return f"{self.nom} igurishwa {self.prix}"
    
class Stock(models.Model):
    id = models.AutoField(primary_key=True)
    created_by = models.ForeignKey(User, on_delete=models.PROTECT)
    produit = models.ForeignKey(Produit, on_delete=models.CASCADE)
    quantinte_initiale = models.FloatField(editable=False, null=True)
    quantinte_actuelle = models.FloatField(editable=False, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    delais_expiration = models.PositiveIntegerField()
    prix = models.FloatField()

class Commande(models.Model):
    id = models.AutoField(primary_key=True)
    created_by = models.ForeignKey(User, on_delete=models.PROTECT)
    prix_total = models.FloatField()
    created_at = models.DateTimeField(auto_now_add=True)
    client = models.CharField(max_length=63)

class ProduitCommande(models.Model):
    id = models.BigAutoField(primary_key=True)
    produit = models.ForeignKey(Produit, on_delete=models.PROTECT)
    commande = models.ForeignKey(Commande, on_delete=models.CASCADE)
    quantite = models.FloatField()
    prix = models.FloatField()

class Paiement(models.Model):
    id = models.AutoField(primary_key=True)
    montant = models.FloatField()
    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(User, on_delete=models.PROTECT)
    commande = models.ForeignKey(Commande, on_delete=models.CASCADE)
