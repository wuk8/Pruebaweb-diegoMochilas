from django.shortcuts import render, redirect
from django.http import JsonResponse
from .models import Mochilas, contacto, comuna, Servicio
from .forms import ContactForm, ServicioConsultaForm


# Create your views here.


def index(request):
    return render(request, 'shop/index.html')

def formulario_contacto(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            
            return redirect('index')  
    else:
        form = ContactForm()
    
    return render(request, 'shop/formularios/formulario_contacto.html', {'form': form})

def guardar_contacto(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            
            return render(request, 'shop/formularios/confirmacion_contacto.html')  # Renderiza la página de confirmación
    else:
        form = ContactForm()
    
    return render(request, 'shop/formularios/formulario_contacto.html', {'form': form})

def consulta_servicios(request):
    form = ServicioConsultaForm(request.GET)
    # pylint: disable=no-member
    servicios = Mochilas.objects.all()

    if form.is_valid():
        nombre_servicio = form.cleaned_data.get('nombre_servicio')
        descripcion = form.cleaned_data.get('descripcion')
        costo_min = form.cleaned_data.get('costo_min')
        costo_max = form.cleaned_data.get('costo_max')
        duracion = form.cleaned_data.get('duracion')
        requisitos = form.cleaned_data.get('requisitos')
        disponibilidad = form.cleaned_data.get('disponibilidad')

        if nombre_servicio:
            servicios = servicios.filter(nombre_servicio__icontains=nombre_servicio)
        
        if descripcion:
            servicios = servicios.filter(descripcion__icontains=descripcion)
        
        if costo_min:
            servicios = servicios.filter(costo__gte=costo_min)
        
        if costo_max:
            servicios = servicios.filter(costo__lte=costo_max)
        
        if duracion:
            servicios = servicios.filter(duracion__icontains=duracion)
        
        if requisitos:
            servicios = servicios.filter(requisitos__icontains=requisitos)
        
        if disponibilidad is not None:
            servicios = servicios.filter(disponibilidad=disponibilidad)

    context = {
        'form': form,
        'servicios': servicios,
    }

    return render(request, 'shop/formularios/consulta_servicios.html', context)

def buscar_servicio(request):
    if request.method == 'GET' and request.is_ajax():
        nombre_servicio = request.GET.get('nombre_servicio', None)

        
        if nombre_servicio:
            # pylint: disable=no-member
            servicios = Servicio.objects.filter(nombre__icontains=nombre_servicio)
        else:
            # pylint: disable=no-member
            servicios = Servicio.objects.all()

        
        resultados = list(servicios.values('nombre', 'descripcion'))

        return JsonResponse(resultados, safe=False)

    
    return JsonResponse({'error': 'Petición inválida'}, status=400)



def mochilas(request):
    nombre_servicio = request.GET.get('nombre_servicio', '')
    precio_min = request.GET.get('precio_min')
    precio_max = request.GET.get('precio_max')

    # pylint: disable=no-member
    mochilas_disponibles = Mochilas.objects.all()

    if nombre_servicio:
        mochilas_disponibles = mochilas_disponibles.filter(nombre__icontains=nombre_servicio)
    
    if precio_min:
        mochilas_disponibles = mochilas_disponibles.filter(precio__gte=precio_min)
    
    if precio_max:
        mochilas_disponibles = mochilas_disponibles.filter(precio__lte=precio_max)

    context = {
        'mochilas_disponibles': mochilas_disponibles,
    }
    return render(request, 'shop/main/mochilas.html', context)


    
def compra(request):
    return render(request, 'shop/navbar/compra.html')

def contactanos(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'shop/navbar/confirmacion.html')  # Redirige a la página de confirmación
    else:
        form = ContactForm()

    context = {
        'form': form,
    }
    return render(request, 'shop/navbar/contactanos.html', context)
