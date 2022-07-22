from tkinter.messagebox import NO
from django.http import Http404
from django.utils.datastructures import MultiValueDictKeyError
from django.shortcuts import render
from campanias.models import Campania, Cedi, Contacto, Pais, Resultado, RegistroExitoso, RegistroNoExitoso, Backup


# Create your views here.


# ##############################################
# VISTA ERROR 404
# ##############################################
def error_not_found(request, exception):
	return render(request, 'formulario/error_404.html')


# ##############################################
# VISTA INDEX
# ##############################################
def index(request):
	cedi = Cedi.objects.all()
	campania = Campania.objects.all()
	pais = Pais.objects.all()

	context = {
		'pais': pais,
		'cedi': cedi,
		'campania': campania,
	}
	return render(request, 'formulario/index.html', context=context)


# TODO: hacer select dependientes


# ##############################################
# VISTA FORMULARIO 
# ##############################################
def formulario(request):
	# se guardan los datos seleccionados con <select>
	cedi_select = request.POST['select_cedis']
	campania_select = request.POST['select_campania']
	pais_select = request.POST['select_pais']

	context = consulta(pais_select, cedi_select, campania_select)

	return render(request, 'formulario/formulario.html', context=context)


# ##############################################
# VISTA SUBMIT REGISTRO
# ##############################################
# El nombre del parámetro deberá ser igual en la vista y en la url, sino 
# desatará un error de submit_registro() got an unexpected keyword argument
def submit_registro(request, cedis, pais, campania, num_dist):
	# * de esta forma no es posible porque da error al no marcar el check
	# * check = request.POST['check_remarcar']

	# obtención de datos
	check = request.POST.get('check_remarcar')

	# Este try es por la funcionalidad de disable con javascript en el archivo main.js, ya que al implementarla,
	# arrojaba ese error. Se hace lo mismo con la variable registro_no_exitoso

	try:
		registro_exitoso = request.POST['registro_exitoso']
	except MultiValueDictKeyError:
		registro_exitoso = None

	try:
		registro_no_exitoso = request.POST['registro_no_exitoso']
	except MultiValueDictKeyError:
		registro_no_exitoso = None

	textarea = request.POST['textarea']

	# si no se hace click en el checkbox, se asigna False
	if not check:
		check = False

	# print(check)
	# print(registro_exitoso)
	# print(num_dist)
	# print(registro_no_exitoso)
	# print(textarea)

	'''
	Primero se obtienen las instancias con las opciones, 
	y estas se ponen en la creación del registro, ya que si 
	se ponen las opciones en directo, da error. 
	'''
	# Obtiene los contactos de campaña, país y CEDIS seleccionados
	contactos = Contacto.objects.filter(pais=pais).filter(cedis=cedis).filter(campania=campania)
	# Obtiene el contacto con los datos seleccionados
	contacto = contactos.get(num_dist=num_dist)

	# si no encuentra registro, le asigna null
	try:
		reg_exi = RegistroExitoso.objects.get(razon=registro_exitoso)
	except RegistroExitoso.DoesNotExist:
		reg_exi = None

	# si no encuentra registro, le asigna null
	try:
		reg_no_exi = RegistroNoExitoso.objects.get(razon=registro_no_exitoso)
	except RegistroNoExitoso.DoesNotExist:
		reg_no_exi = None

	id_contacto = Contacto.objects.get(id=contacto.id)

	# confirma que el contacto ya exista en el modelo Resultado
	existe_en_resultado = Resultado.objects.filter(contacto=id_contacto).exists()

	# Si existe en resultado, actualiza el registro (vuelve a reescribir el contacto), y se modifica
	# automáticamente la hora de actualización. Si el registro aún
	# no existe en el modelo Resultado, lo crea.
	if existe_en_resultado:
		reg = Resultado.objects.get(contacto=id_contacto)
		reg.contacto = contacto
		reg.registro_no_exi = reg_no_exi
		reg.registro_exi = reg_exi
		reg.comentario = textarea
		reg.remarcar = check
		reg.save()
	else:
		registro = Resultado(contacto=id_contacto, registro_no_exi=reg_no_exi, registro_exi=reg_exi,
		                     comentario=textarea,
		                     remarcar=check)
		registro.save()

	# *****************************************************************
	# CONTEO DE REGISTROS
	# ****************************************************************
	# Obtiene el conteo de los contactos totales de esa campaña y cedis seleccionados
	registros_totales = contactos.count()
	# Obtiene los contactos de Resultado que sean de la campaña y CEDIS seleccionado, después los filtra por remarcar
	# y al final los cuenta
	total_no_exitosos = Resultado.objects.filter(contacto__in=contactos).filter(remarcar=True).count()
	# Obtiene los contactos de Resultado que sean de la campaña y CEDIS seleccionado, después los filtra por no remarcar
	# y al final los cuenta
	total_exitosos = Resultado.objects.filter(contacto__in=contactos).filter(remarcar=False).count()
	# obtiene los registros totales sin marcar
	total_sin_marcar = registros_totales - (total_exitosos + total_no_exitosos)
	# ****************************************************************

	context = {
		'cedis': cedis,
		'pais': pais,
		'campania': campania,
		'registros_totales': registros_totales,
		'total_no_exitosos': total_no_exitosos,
		'total_exitosos': total_exitosos,
		'total_sin_marcar': total_sin_marcar,
	}

	# se crean instancias de los modelos Contacto y Resultado
	# para poder hacer los registros en el modelo Backup

	# contac = Contacto.objects.get(num_dist=num_dist)
	result = Resultado.objects.get(contacto=id_contacto)

	# registro en el modelo Backup del contacto en cuestión
	# contacto = contac
	Backup(
		num_dist=num_dist,
		nombres=contacto.nombre,
		descuento_choice=contacto.descuento_choice,
		tel_casa=contacto.tel_casa,
		tel_cel=contacto.tel_cel,
		pais=contacto.pais,
		estado=contacto.estado,
		centro_alta=contacto.centro_alta,
		email=contacto.email,
		fecha_ultima_compra=contacto.fecha_ultima_compra,
		meses_sin_compra=contacto.meses_sin_compra,
		fecha_alta=contacto.fecha_alta,
		sexo=contacto.sexo,
		fecha_nacimiento=contacto.fecha_nacimiento,
		total_puntos=contacto.total_puntos,
		campania=campania,
		cedi=cedis,
		registro_no_exi=registro_no_exitoso,
		registro_exi=registro_exitoso,
		comentario=result.comentario,
		remarcar=result.remarcar
	).save()
	return render(request, 'formulario/submit_registro.html', context=context)


# ##############################################
# VISTA FORMULARIO 2
# ##############################################
def formulario2(request, pais, cedis, campania, registros_totales, total_no_exitosos, total_exitosos):
	pais_select = pais
	cedi_select = cedis
	campania_select = campania

	context = consulta(pais_select, cedi_select, campania_select)
	context['registros_totales'] = registros_totales
	context['total_no_exitosos'] = total_no_exitosos
	context['total_exitosos'] = total_exitosos

	return render(request, 'formulario/formulario2.html', context=context)


# ##############################################
# FUNCTION consulta
# ############################################


'''
Para evitar repetir código en las vistas formulario y formulario2, 
se crea la función consulta para proveerles el contexto, ya que en 
ambas es el mismo.
'''


def consulta(pais, cedi, campania):
	pais_select = pais
	cedi_select = cedi
	campania_select = campania

	# QUERYSET: filtra las campañas por el nombre seleccionado y muestra su campo descripcion
	descripcion_campania = Campania.objects.get(nombre=campania_select)  # .values('descripcion')
	# print(descripcion_campania)

	# obtiene los querysets de los contactos que son de la campaña y cedis seleccionado
	lista_contactos = Contacto.objects.filter(campania=campania_select).filter(cedis=cedi_select).filter(
		pais=pais_select)
	# lista_contactos = get_object_or_404(campania=campania_select).filter(cedis=cedi_select)

	# devuelve los querysets de la lista_contactos que están en el campo contacto de tabla Resultado y
	# sobre de ellos filtra los que están por remarcar
	por_remarcar = Resultado.objects.filter(contacto__in=lista_contactos).filter(remarcar=True)

	# devuelve los querysets de los contactos seleccionados que no están aún en la tabla Resultado
	sin_marcar = lista_contactos.exclude(id__in=Resultado.objects.values('contacto'))

	remarcar_excluidos = sin_marcar.filter(cedis=cedi_select).filter(campania=campania_select)

	# si en la tabla Contactos hay contactos que aún no existen en la tabla Resultado,
	# devuelve uno de ellos, sino, devuelve un contacto que está en la tabla resultado
	# con el campo remarcar como True

	def contacto_pormarcar():

		# Si hay contactos que aún no están en el modelo resultado,
		# los devuelve. Si no, devuelve el contacto más antiguo (que se
		# ingresó primero) que esté en el modelo Resultado
		if remarcar_excluidos.count() > 0:
			return remarcar_excluidos[0]
		elif por_remarcar.count() > 0:
			i = por_remarcar.earliest('ultima_interaccion')
			return i

	contacto = contacto_pormarcar()
	# print('contacto: ', contacto)

	cts = Contacto.objects.filter(campania=campania_select).filter(cedis=cedi_select).filter(pais=pais_select)

	# si no existen registros para la consulta, levanta un 404:
	try:
		contacto = cts.get(num_dist=contacto)
	except Contacto.DoesNotExist:
		raise Http404

	# Se obtienen los registros exitosos y no exitosos para poderlos
	# elegir en el frontend
	registros_exitosos = RegistroExitoso.objects.all()
	registros_no_exitosos = RegistroNoExitoso.objects.all()

	# creación de contexto
	context = {
		'pais_select': pais_select,
		'cedi_select': cedi_select,
		'campania_select': campania_select,
		'descripcion_campania': descripcion_campania,
		'contacto': contacto,
		'registros_exitosos': registros_exitosos,
		'registros_no_exitosos': registros_no_exitosos,
	}

	return context
