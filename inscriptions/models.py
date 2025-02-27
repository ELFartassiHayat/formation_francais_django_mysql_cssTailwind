from django.db import models

class Inscription(models.Model):
    nom = models.CharField(max_length=100)
    prenom = models.CharField(max_length=100)
    email = models.EmailField()
    niveau = models.CharField(max_length=50, choices=[
        ('débutant', 'Débutant'),
        ('intermédiaire', 'Intermédiaire'),
        ('avancé', 'Avancé'),
    ])
    telephone = models.CharField(max_length=20)

    def __str__(self):
        return f"{self.prenom} {self.nom}"