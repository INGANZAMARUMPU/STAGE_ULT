from django.contrib import admin
from .models import *

admin.site.register(Produit)
admin.site.register(Stock)
admin.site.register(Commande)
admin.site.register(ProduitCommande)
admin.site.register(Paiement)
