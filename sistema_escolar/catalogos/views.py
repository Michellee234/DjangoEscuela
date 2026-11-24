from django.shortcuts import render, redirect
from catalogos.models import Carrera
from catalogos.forms import CarreraForm


def inicio(request):
    return render(request, 'catalogos/index.html')


def listarCarreras(request):
    # Se recuperan los registros del modelo Carrera
    carreras = Carrera.objects.all()

    # Se construye el diccionario que se enviará al html
    data = {'carreras': carreras}

    # Generar la renderización
    return render(request, 'catalogos/listarCarreras.html', data)


def crearCarreras(request):
    if request.method == 'POST':        # Se presionó el botón de guardar
        form = CarreraForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listarCarreras')
    else:
        form = CarreraForm()            # Se abre el formulario para captura
    return render(request, 'catalogos/crearCarrera.html', {'form': form})

#------------clase 24
def editarCarreras(request, pk):
    carrera= Carrera.objects.get(pk=pk)
    if request.method=='GET':
        form=CarreraForm(instance=carrera)
    else: 
        form= CarreraForm(request.POST, instance=carrera)
        if form.is_valid():
            form.save()
        return redirect ('listarCarerras')
    return render (request, 'crearCarrera.html', {'form':form})

def eliminarCarreras(request, pk):
    carrera=Carrera.objects.get(pk=pk)
    if request.method== 'POST':
        carrera.delete()
        return redirect ('listarCarreras')
    
    return render (request, 'eliminarCarreras.html', {'carrera':carrera})