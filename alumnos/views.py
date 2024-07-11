from django.shortcuts import render, redirect
from .models import Alumno, Genero
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout


@login_required
def index(request):
    alumnos = Alumno.objects.all()
    context = {"alumnos": alumnos}
    return render(request, 'alumnos/index.html', context)
@login_required

def paciente_list(request):
    alumnos = Alumno.objects.all()
    context = {'alumnos': alumnos}
    return render(request, 'alumnos/paciente_list.html', context)

@login_required
def paciente_add(request):
    if request.method != "POST":
        generos = Genero.objects.all()
        context = {'generos': generos}
        return render(request, 'alumnos/paciente_add.html', context)
    else:
        rut = request.POST["rut"]
        nombre = request.POST["nombre"]
        aPaterno = request.POST["paterno"]
        aMaterno = request.POST["materno"]
        fechaNac = request.POST["fechaNac"]
        genero = request.POST["genero"]
        telefono = request.POST["telefono"]
        email = request.POST["email"]
        direccion = request.POST["direccion"]
        activo = "1"
        objGenero = Genero.objects.get(id_genero=genero)
        obj = Alumno.objects.create(
            rut=rut,
            nombre=nombre,
            apellido_paterno=aPaterno,
            apellido_materno=aMaterno,
            fecha_nacimiento=fechaNac,
            id_genero=objGenero,
            telefono=telefono,
            email=email,
            direccion=direccion,
            activo=1
        )
        obj.save()
        context = {'mensaje': "OK, datos grabados..."}
        return render(request, 'alumnos/paciente_add.html', context)
    
@login_required
def paciente_del(request, pk):
    context = {}
    try:
        alumno = Alumno.objects.get(rut=pk)
        alumno.delete()
        mensaje = "Bien, datos eliminados..."
    except Alumno.DoesNotExist:
        mensaje = "Error, rut no existe..."
    alumnos = Alumno.objects.all()
    context = {'alumnos': alumnos, 'mensaje': mensaje}
    return render(request, 'alumnos/paciente_list.html', context)

@login_required
def paciente_findEdit(request, pk):
    try:
        alumno = Alumno.objects.get(rut=pk)
        generos = Genero.objects.all()
        context = {'alumno': alumno, 'generos': generos}
        return render(request, 'alumnos/paciente_edit.html', context)
    except Alumno.DoesNotExist:
        context = {'mensaje': "Error, rut no existe..."}
        return render(request, 'alumnos/paciente_list.html', context)



@login_required
def pacienteUpdate(request):
    if request.method == "POST":
        rut = request.POST["rut"]
        nombre = request.POST["nombre"]
        aPaterno = request.POST["paterno"]
        aMaterno = request.POST["materno"]
        fechaNac = request.POST["fechaNac"]
        genero = request.POST["genero"]
        telefono = request.POST["telefono"]
        email = request.POST["email"]
        direccion = request.POST["direccion"]
        activo = "1"

        objGenero = Genero.objects.get(id_genero=genero)
        alumno = Alumno.objects.get(rut=rut)

        alumno.nombre = nombre
        alumno.apellido_paterno = aPaterno
        alumno.apellido_materno = aMaterno
        alumno.fecha_nacimiento = fechaNac
        alumno.id_genero = objGenero
        alumno.telefono = telefono
        alumno.email = email
        alumno.direccion = direccion
        alumno.activo = activo
        alumno.save()

        context = {'mensaje': "OK, datos actualizados...", 'generos': Genero.objects.all(), 'alumno': alumno}
        return render(request, 'alumnos/paciente_edit.html', context)
    else:
        alumnos = Alumno.objects.all()
        context = {'alumnos': alumnos}
        return render(request, 'alumnos/paciente_list.html', context)
    

def salir(request):

    logout(request)
    return redirect('index')
