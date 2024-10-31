from django.shortcuts import render



def index(request):
    return render(request, 'index.html')


def kategors(request):
    return render(request, 'kategors.html')


# Create your views here.
