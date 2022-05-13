from django.shortcuts import render
from campanias.models import Campania

# Create your views here.
def index(request):
    campanias = Campania.objects.all()
    context = {'campania': campanias}
    return render(request, 'formulario/index.html', context=context)

def submit(request):
    return render(request, 'formulario/submit.html')


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