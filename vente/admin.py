from django.contrib import admin
from .models import *


@admin.register(Produit)
class ProduitAdmin(admin.ModelAdmin):
    list_display = "nom", "unite", "quantite", "prix"
    
@admin.register(Stock)
class StockAdmin(admin.ModelAdmin):
    list_display = "created_by", "produit", "quantite_initiale", "quantite_actuelle", "created_at", "delais_expiration", "prix"

@admin.register(Commande)
class CommandeAdmin(admin.ModelAdmin):
    list_display = "created_by", "prix_total", "created_at", "client"

@admin.register(ProduitCommande)
class ProduitCommandeAdmin(admin.ModelAdmin):
    list_display = "produit", "commande", "quantite", "prix"

@admin.register(Paiement)
class PaiementAdmin(admin.ModelAdmin):
    list_display = "montant", "created_at", "created_by", "commande"


