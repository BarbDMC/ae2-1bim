from django.shortcuts import render, redirect, get_object_or_404
from .models import ParqueNatural, GuiaTuristico, Recorrido
from .forms import ParqueForm, GuiaForm, RecorridoForm

def listar_parques(request):
    parques = ParqueNatural.objects.all()
    return render(request, 'parque/listar_parques.html', {'parques': parques})

def crear_parque(request):
    form = ParqueForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('listar_parques')
    return render(request, 'parque/formulario.html', {'form': form})

def editar_parque(request, pk):
    parque = get_object_or_404(ParqueNatural, pk=pk)
    form = ParqueForm(request.POST or None, instance=parque)
    if form.is_valid():
        form.save()
        return redirect('listar_parques')
    return render(request, 'parque/formulario.html', {'form': form})

def listar_guias(request):
    guias = GuiaTuristico.objects.all()
    return render(request, 'parque/listar_guias.html', {'guias': guias})

def crear_guia(request):
    form = GuiaForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('listar_guias')
    return render(request, 'parque/formulario.html', {'form': form})

def listar_recorridos(request):
    recorridos = Recorrido.objects.all()
    return render(request, 'parque/listar_recorridos.html', {'recorridos': recorridos})

def crear_recorrido(request):
    form = RecorridoForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('listar_recorridos')
    return render(request, 'parque/formulario.html', {'form': form})
