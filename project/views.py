from django.shortcuts import render



def index(request):
    return render(request, 'index.html')


def search(request):
    return render(request, 'search.html')


def haryt_profil(request):
    return render(request, 'haryt_profil.html')



def list(request):
    return render(request, 'list.html')

# Create your views here.
