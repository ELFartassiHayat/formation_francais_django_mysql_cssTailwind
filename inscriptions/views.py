from django.shortcuts import render, redirect
from .forms import InscriptionForm
from django.core.mail import send_mail

def inscription(request):
    if request.method == 'POST':
        form = InscriptionForm(request.POST)
        if form.is_valid():
            form.save()
            whatsapp_url = f"https://wa.me/+212777285474?text=Bonjour,%20je%20souhaite%20m'inscrire%20à%20votre%20formation%20en%20français.%20Pouvez-vous%20me%20donner%20plus%20d'informations%20?"
            return redirect(whatsapp_url)
    else:
        form = InscriptionForm()
    return render(request, 'inscriptions/inscription.html', {'form': form})

def accueil(request):
    return render(request, 'inscriptions/accueil.html')