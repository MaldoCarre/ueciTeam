from django.shortcuts import render


# imports django-restFrameworks
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Denuncia,Departamentos,Tipo_ciberdelito,Tipo_incidente,Plataforma,Imagenes
from.serializers import DenunciaSerializada,DepartamentosSerializada,TipociberdelitoSerializada,TipoincidenteSerializada,PataformaSerializada
from django.core.files.storage import FileSystemStorage

# Create your views here.

#Prueba rest
@api_view(['GET'])
def jsonfunction (request):
    denuncias = Denuncia.objects.all()
    contador = 0 
    for i in denuncias:
        contador+=1
    contexto = contador

    api_variable = {
        'cantidad':contexto
    }
    return Response(api_variable)


# CRUD de los reportes / denuncias 


# Listando Denuncias
@api_view(['GET'])
def listaDenuncias(request):
    model = Denuncia.objects.all()
    serializer = DenunciaSerializada(model, many=True)
    return Response(serializer.data)

# Carga de la denuncia
@api_view(['POST'])
def cargaDenuncia (request):
    mail = request.POST.get("mail")
    nombre = request.POST.get("nombre")
    apellido = request.POST.get("apellido")
    telefono = request.POST.get("telefono")
    departamento = request.POST.get("departamento")
    ciberdelito = request.POST.get("ciberdelito")
    incidente = request.POST.get("incidente")
    lugarDeDenuncia = request.POST.get("lugarDeDenuncia")
    plataforma = request.POST.get("plataforma")
    url_evidencia = request.POST.get("url_evidencia")
    denuncia = request.POST.get("denuncia")
    observacion = request.POST.get("observacion")
    imagenes = request.FILES.getlist("imagenes[]")
    denunciaueci = Denuncia(mail=mail,nombre=nombre,apellido=apellido,telefono=telefono,departamento=departamento,ciberdelito=ciberdelito,incidente=incidente,denuncia=denuncia,plataforma=plataforma,url_evidencia=url_evidencia,observacion=observacion,lugarDeDenuncia=lugarDeDenuncia)
    denunciaueci.save()
    for img in imagenes:
        fs = FileSystemStorage()
        file_path=fs.save(img.name,img)
        imagen = Imagenes(denuncia=denunciaueci,imagenes=file_path)
        imagen.save()


    #serializer = DenunciaSerializada(data=request.data)
    #if serializer.is_valid():
    #    serializer.save()
    return Response("Archivo cargado")

# Editar la denuncia

@api_view(['POST'])
def editar (request,id):
    model = Denuncia.objects.get(id=id)
    serializer = DenunciaSerializada(instance=model,data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

# Eliminar la denuncia
@api_view(['DELETE'])
def eliminar(request,id):
    model = Denuncia.objects.get(id=id)
    model.delete()
    return Response('Objeto correctamente eliminado')
# --------------------------------------------------------------------------------------


# CRUD DE LOS DEPARTAMENTOS

#lista departamentos de La Rioja.
@api_view(['GET'])
def listaDepartamentos (request):
    model = Departamentos.objects.all()
    serializer = DepartamentosSerializada(model, many=True)
    return Response(serializer.data)

# Carga departamentos.
@api_view(['POST'])
def cargaDepartamento (request):
    serializer = DepartamentosSerializada(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

# Editar departamentos.
@api_view(['POST'])
def editarDepartamento(request,id):
    model = Departamentos.objects.get(id=id)
    serializer = DepartamentosSerializada(instance=model, data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

#Eliminar departamentos.
@api_view(['DELETE'])
def eliminarDepartamento(reques,id):
    model = Departamentos.objects.get(id = id)
    model.delete()
    return Response("Departamento eliminado con exito")

# ------------------------------------------------------------------------------

# Crud de Tipo de ciberdelito .
#listando ciberdelito.
@api_view(['GET'])
def listaCiberdelito (reques):
    model = Tipo_ciberdelito.objects.all()
    serializer = TipociberdelitoSerializada(model , many=True)
    return Response(serializer.data)

#Carga Ciberdelito.
@api_view(['POST'])
def cargaciberdelito (requets):
    serializer = TipociberdelitoSerializada(data=requets.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

# Editar el ciberdelito
@api_view(['POST'])
def editarCiberdelito (requets,id):
    model = Tipo_ciberdelito.objects.get(id = id)
    serializer = TipociberdelitoSerializada(instance=model , data=requets.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

# Eliminar Ciberdelito
def elminarciberdelito(requets,id):
    model = Tipo_ciberdelito.objects.get(id = id)
    model.delete()
    return Response("El cibedelito fue eliminado con exito")


#--------------------------------------------------------------------------------

#Crud de el tipo de incidente

#listado de incidentes
@api_view(['GET'])
def listartipoincidente(request):
    model = Tipo_incidente.objects.all()
    serializer=TipoincidenteSerializada(model,many=True)
    return Response(serializer.data)
#Carga Incidente
@api_view(['POST'])
def cargaIncidente(request):
    serializer = TipoincidenteSerializada(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)
# Edita Incidente 
@api_view(['POST'])
def editaincidente(request,id):
    model = Tipo_incidente.objects.get(id = id)
    serializer = TipociberdelitoSerializada(instance=model,data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

#Eliminar incidente
@api_view(['DELETE'])
def eliminarincidente(request,id):
    model = Tipo_incidente.objects.get(id = id)
    model.delete()
    return Response("El incidente fue eliminado con exito")
