from django.shortcuts import render


def inicio(request):
    return render(request, 'tutorias/index.html')

# Create your views here.
