from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.core.checks import messages
from django.shortcuts import render, redirect
from .models import Korisnik


# Create your views here.
def prva(request):
    return render(request, "prva.html")
def registracija(request):

    return render(request, 'register.html')

def logiranje(request):
    return render(request, "login.html")
def test(request):
    return render(request, "test.html")
def pocetna(request):
    return render(request, "pocetna.html")
def testiranje(request):
    return render(request, "testiranje.html")
def sodrzina(request):
    return render(request, "sodrzina.html")
def kviz(request):
    return render(request, "kviz.html")
def rez_kviz(request):
    return render(request, "rez_k.html")
def rez_testiranje(request):
    return render(request, "rez_t.html")


def prva_register(request):
    return redirect('registration')
def prva_logiranje(request):
    return redirect('login')
def logiranje_prva(request):
    return redirect('home')
def registracija_prva(request):
    return redirect('home')
def test_testiranje(request):
    return redirect('testiranje')
def test_pocetna(request):
    return redirect('pocetna')
def registracija_pocetna(request):
    return redirect('pocetna')
def logiranje_pocetna(request):
    return redirect('pocetna')
def testiranje_pocetna(request):
    return redirect('pocetna')
def testiranje_pocetna(request):
    return redirect('pocetna')

def testiranje_rezultati(request):
    return redirect('rezt')
def kviz_rezultati(request):
    return redirect('rezk')
def sodrzina_pocetna(request):
    return redirect('pocetna')
def rezultatik_pocetna(request):
    return redirect('pocetna')
def rezultatit_pocetna(request):
    return redirect('pocetna')