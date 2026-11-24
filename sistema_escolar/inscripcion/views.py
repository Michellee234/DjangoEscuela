from django.shortcuts import render

def inicio(request):
    return render(request, 'inscripcion/index.html')

# Create your views here.
