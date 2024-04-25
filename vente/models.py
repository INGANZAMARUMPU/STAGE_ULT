from django.db import models
from django.contrib.auth.models import User

class Produit(models.Model):
    id = models.AutoField(primary_key=True)
    nom = models.CharField(max_length=31)
    unite = models.CharField(max_length=31)
    quantite = models.FloatField(editable=False, null=True)
    prix = models.FloatField()

    def __str__(self):
        return f"{self.nom} igurishwa {self.prix}"
    
class Stock(models.Model):
    id = models.AutoField(primary_key=True)
    created_by = models.ForeignKey(User, on_delete=models.PROTECT)
    produit = models.ForeignKey(Produit, on_delete=models.CASCADE)
    quantite_initiale = models.FloatField(default=0)
    quantite_actuelle = models.FloatField(editable=False, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    delais_expiration = models.PositiveIntegerField()
    prix = models.FloatField()

    def __str__(self) -> str:
        return f"{self.quantite_initiale} {self.produit.unite} de {self.produit}"

class Commande(models.Model):
    id = models.AutoField(primary_key=True)
    created_by = models.ForeignKey(User, on_delete=models.PROTECT)
    prix_total = models.FloatField()
    created_at = models.DateTimeField(auto_now_add=True)
    client = models.CharField(max_length=63)

    def __str__(self) -> str:
        return f"Commande de {self.created_by} valant {self.prix_total}"

class ProduitCommande(models.Model):
    id = models.BigAutoField(primary_key=True)
    produit = models.ForeignKey(Produit, on_delete=models.PROTECT)
    commande = models.ForeignKey(Commande, on_delete=models.CASCADE)
    quantite = models.FloatField()
    prix = models.FloatField()

    def __str__(self) -> str:
        return f"{self.quantite} {self.produit.unite} de {self.produit}"

class Paiement(models.Model):
    id = models.AutoField(primary_key=True)
    montant = models.FloatField()
    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(User, on_delete=models.PROTECT)
    commande = models.ForeignKey(Commande, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return f"{self.montant} sur {self.commande} à {self.created_by}"
