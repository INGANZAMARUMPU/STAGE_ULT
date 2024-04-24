from django.db import models

class Category(models.Model):
    id = models.AutoField(primary_key=True)
    nom = models.CharField(max_length=31)

    def __str__(self):
        return self.nom

class Produit(models.Model):
    id = models.AutoField(primary_key=True)
    nom = models.CharField(max_length=31)
    unite = models.CharField(max_length=31)
    quantinte = models.FloatField(editable=False, null=True)
    prix_vente = models.FloatField()
    category = models.ForeignKey(Category, null=True, on_delete=models.SET_NULL)

    def __str__(self):
        return f"{self.nom} igurishwa {self.prix_vente}"



