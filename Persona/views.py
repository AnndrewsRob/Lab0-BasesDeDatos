from django.shortcuts import render, redirect
from .models import Persona
from django.contrib import messages



def home(request):
    personas = Persona.objects.all()
    messages.success(request, '¡Personas listadas!')
    return render(request, 'gestionPersonas.html',{'personas':personas})

from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Persona


def registrarPersona(request):
    if request.method == 'POST':
        idPersona = request.POST['txtNumeroIdentificacion']
        tipo_de_documento = request.POST['txtDocumento']
        nombre = request.POST['txtNombre']
        apellido = request.POST['txtApellido']
        telefono = request.POST['txtTelefono']
        sexo = request.POST.get('selectSexo')
        edad = request.POST['txtEdad']
        id_responsable = request.POST['txtCabezaIdentificacion']

        if Persona.objects.filter(idPersona=idPersona).exists():
            messages.error(request, 'El ID ya está en uso.')
            return redirect('/')
        
        # Crear la persona sin un responsable
        persona = Persona.objects.create(
            idPersona=idPersona,
            idResponsable=None,  # No hay responsable, ya que es la cabeza de familia
            tipo_de_documento=tipo_de_documento,
            nombre=nombre,
            apellido=apellido,
            telefono=telefono,
            sexo=sexo,
            edad=edad
        )

        if id_responsable and id_responsable == idPersona:
            # Si el ID del responsable directo es igual al ID de la persona misma,
            # establecer la relación de llave foránea a sí mismo
            persona.idResponsable = persona
            persona.save()
        elif id_responsable:
            try:
                id_responsable_directo = int(id_responsable)
                responsable_directo = Persona.objects.get(pk=id_responsable_directo)
                persona.idResponsable = responsable_directo
                persona.save()
            except (ValueError, Persona.DoesNotExist):
                pass  # Si no se puede encontrar el responsable directo, no hacer nada

        messages.success(request, '¡Persona registrada!')
        return redirect('/')
    else:
        return render(request, 'gestionPersonas.html')



def edicionPersona(request,idPersona):
    persona = Persona.objects.get(idPersona=idPersona)
    return render(request, "edicionPersona.html", {"persona": persona})

def editarPersona(request, idPersona):
    tipo_de_documento = request.POST['txtDocumento']
    nuevo_idPersona = request.POST['txtNumeroIdentificacion']
    nombre = request.POST['Nombre']
    apellido = request.POST['Apellido']
    telefono = request.POST['telefono']
    sexo = request.POST['sexo']
    edad = request.POST['edad']
    id_responsable = request.POST.get('txtCabezaIdentificacion')

    responsable_directo = None
    if id_responsable:
        try:
            id_responsable_directo = int(id_responsable)
            responsable_directo = Persona.objects.get(pk=id_responsable_directo)
        except (ValueError, Persona.DoesNotExist):
            pass

    if Persona.objects.filter(idPersona=nuevo_idPersona).exclude(idPersona=idPersona).exists():
        messages.error(request, 'El nuevo ID ya está en uso.')
        return redirect(f'/edicionPersona/{idPersona}/')

    persona = Persona.objects.get(idPersona=idPersona)

    persona.idPersona = nuevo_idPersona
    persona.tipo_de_documento = tipo_de_documento
    persona.nombre = nombre
    persona.apellido = apellido
    persona.telefono = telefono
    persona.sexo = sexo
    persona.edad = edad
    persona.idResponsable = responsable_directo

    persona.save()

    messages.success(request, '¡Persona actualizada!')
    return redirect('/')

def eliminarPersona(request, idPersona):
    persona = Persona.objects.get(idPersona=idPersona)
    persona.delete()
    messages.success(request, '¡Persona eliminado!')

    return redirect('/')