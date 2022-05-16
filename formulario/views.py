from django.shortcuts import redirect, render
from campanias.models import Campania, Cedi

# Create your views here.

# **********************************************
# VISTA INDEX
# **********************************************
def index(request):
    cedi = Cedi.objects.all()
    campanias = Campania.objects.all()
    #campanias = Campania.objects.filter(cedis = cedi[0])
    # campanias = Campania.objects.select_related('cedis').filter(cedis=cedi)
    context = {
        'campania': campanias,
        'cedi': cedi,
    }
    return render(request, 'formulario/index.html', context=context)


#def despliega_campania(request):


# **********************************************
# VISTA FORMULARIO
# **********************************************
def formulario(request):
    cedi = request.POST['select_cedis']
    campania = request.POST['select_campania']
    print(cedi)
    print(campania)
    return render(request, 'formulario/formulario.html')


# ******************************************************
# VISTA DE FORMULARIO
# ******************************************************
# from .forms import ContactoForm

# def index(request):
#     context={}
#     if request.method == 'POST':
#         form = ContactoForm(request.POST or None, request.FILES or None)
#         if form.is_valid():
#             # process the data in form.cleaned_data as required
#             #nombres = form.cleaned_data['nombres']
#             # ...
#             # redirect to a new URL:
#             form.save()

#      # if a GET (or any other method) we'll create a blank form
#     else:
#         form = ContactoForm()
#     context['form'] = form
#     return render(request, 'formulario/index.html', context)