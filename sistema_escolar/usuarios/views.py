from django.shortcuts import render

def inicio(request):
    return render(request, 'usuarios/index.html')

# Create your views here.
