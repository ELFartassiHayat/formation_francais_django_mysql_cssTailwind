from django.contrib import admin
from .models import Inscription

class InscriptionAdmin(admin.ModelAdmin):
    list_display = ('nom', 'prenom', 'email', 'niveau', 'telephone') #Définit les champs à afficher dans la liste des inscriptions.
    list_filter = ('niveau',) #Ajoute des filtres pour faciliter la recherche.
    search_fields = ('nom', 'prenom', 'email') #  rechercher des inscriptions par nom, prénom ou e-mail.

admin.site.register(Inscription, InscriptionAdmin)