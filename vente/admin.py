from typing import Any
from django.contrib import admin, messages
from django.db.models.query import QuerySet
from django.http import HttpRequest
from django.utils.safestring import mark_safe
from .models import *

admin.site.site_header = "KIOSK SAINT KIZITO"


@admin.register(Produit)
class ProduitAdmin(admin.ModelAdmin):
    list_display = "nom", "unite", "quantite", "prix", "options"
    search_fields = "nom",

    def options(self, obj:Produit):
        return mark_safe(f"<a href='/admin/vente/stock/?produit__id__exact={obj.id}'>voir stock</a>")
    
@admin.register(Stock)
class StockAdmin(admin.ModelAdmin):
    list_display = "produit", "created_by", "quantite_initiale", "quantite_actuelle",

    def save_model(self, request, obj: Stock, form, change) -> None:
        if change:
            messages.add_message(request, messages.ERROR, "modification ntikunda")
            return
        produit = obj.produit
        try:
            produit.quantite += obj.quantite_initiale
        except Exception:
            produit.quantite = obj.quantite_initiale
        produit.save()
        obj.quantite_actuelle = obj.quantite_initiale
        obj.created_by = request.user
        return super().save_model(request, obj, form, change)
    
    def delete_model(self, request, obj:Stock):
        produit = obj.produit
        produit.quantite -= obj.quantite_actuelle
        produit.save()
        return super().delete_model(request, obj)
    
    def delete_queryset(self, request, queryset: QuerySet[Stock]):
        for obj in queryset:
            produit = obj.produit
            produit.quantite -= obj.quantite_actuelle
            produit.save()
        return super().delete_queryset(request, queryset)

@admin.register(Commande)
class CommandeAdmin(admin.ModelAdmin):
    list_display = "created_by", "prix_total", "created_at", "client"

@admin.register(ProduitCommande)
class ProduitCommandeAdmin(admin.ModelAdmin):
    list_display = "produit", "commande", "quantite", "prix"
    list_filter = "produit",

    def save_model(self, request, obj:ProduitCommande, form, change):
        if change:
            messages.add_message(request, messages.ERROR, "modification ntikunda")
            return
        produit = obj.produit
        if obj.quantite > (produit.quantite or 0):
            messages.add_message(request, messages.ERROR, f"{produit} hasigaye {produit.quantite or 0} {produit.unite} gusa")
            return

        commande = Commande.objects.filter(done=False).first()
        if not commande:
            # commande = INSERT INTO Commande(created_by) VALUES (request.user)
            commande = Commande.objects.create(created_by = request.user)
        obj.commande = commande
        obj.prix = obj.produit.prix * obj.quantite
        commande.prix_total += obj.prix
        commande.save()
        return super().save_model(request, obj, form, change)
    
    def delete_model(self, request, obj: ProduitCommande) -> None:
        commande = obj.commande
        commande.prix_total -= obj.prix
        commande.save()
        return super().delete_model(request, obj)
    
    def delete_queryset(self, request, queryset: QuerySet[ProduitCommande]) -> None:
        for obj in queryset:
            commande = obj.commande
            commande.prix_total -= obj.prix
            commande.save()
        return super().delete_queryset(request, queryset)

@admin.register(Paiement)
class PaiementAdmin(admin.ModelAdmin):
    list_display = "montant", "created_at", "created_by", "commande"


