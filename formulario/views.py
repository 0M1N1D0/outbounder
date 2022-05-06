from unicodedata import name
from django.shortcuts import render, HttpResponseRedirect

# Create your views here.
def index(request):
    context = {}
    return render(request, 'formulario/index.html', context=context)


# ******************************************************
# VISTA DE FORMULARIO
# ******************************************************
from .forms import ContactoForm

def get_contacto(request):
    context={}
    if request.method == 'POST':
        form = ContactoForm(request.POST or None, request.FILES or None)
        if form.is_valid():
            # process the data in form.cleaned_data as required
            #nombres = form.cleaned_data['nombres']
            # ...
            # redirect to a new URL:
            form.save()

     # if a GET (or any other method) we'll create a blank form
    else:
        form = ContactoForm()
    context['form'] = form
    return render(request, 'formulario/index.html', context)