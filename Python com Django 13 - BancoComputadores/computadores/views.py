from django.shortcuts import render, redirect, get_object_or_404
from .models import Computador
from .forms import ComputadorForm

def lista_computadores(request):
    query = request.GET.get('q')
    if query:
        computadores = Computador.objects.filter(
            fabricante__icontains=query
        ) | Computador.objects.filter(
            processador__icontains=query
        ) | Computador.objects.filter(
            memoria_ram__icontains=query
        ) | Computador.objects.filter(
            armazenamento__icontains=query
        ) | Computador.objects.filter(
            placa_video__icontains=query
        )
    else:
        computadores = Computador.objects.all()
    
    return render(request, 'computadores/lista.html', {'computadores': computadores, 'query': query})


def adicionar_computador(request):
    if request.method == "POST":
        form = ComputadorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_computadores')
    else:
        form = ComputadorForm()
    return render(request, 'computadores/adicionar.html', {'form': form})

def editar_computador(request, id):
    computador = get_object_or_404(Computador, id=id)
    if request.method == "POST":
        form = ComputadorForm(request.POST, instance=computador)
        if form.is_valid():
            form.save()
            return redirect('lista_computadores')
    else:
        form = ComputadorForm(instance=computador)
    return render(request, 'computadores/editar.html', {'form': form, 'computador': computador})

def excluir_computador(request, id):
    computador = get_object_or_404(Computador, id=id)
    if request.method == "POST":
        computador.delete()
        return redirect('lista_computadores')
    return render(request, 'computadores/excluir.html', {'computador': computador})

