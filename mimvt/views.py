from django.shortcuts import render

from django.forms import CharField
from django.http import HttpResponse

from .models import direcciones, familiares, profesiones




def familiar(request,nombre,apellido,dni):
    mis_nombre= familiares(nombre=nombre,apellido=apellido,dni=dni)
    mis_nombre.save()
    
    return HttpResponse(f'Hola mi familiar es {mis_nombre.nombre} {mis_nombre.apellido} y su dni es: {mis_nombre.dni} ')

def profesion(request,profesion):
    mi_profesion= profesiones(profesion=profesion)
    mi_profesion.save()
    
    return HttpResponse(f'Su profesion es {mi_profesion.profesion}')

def direccion(request,calle, localidad,cp):
    mi_direccion= direcciones(calle=calle, localidad=localidad, cp=cp)
    mi_direccion.save()
    
    return HttpResponse(f'Su direccion es: {mi_direccion.calle} ,localidad: {mi_direccion.localidad} y cp: {mi_direccion.cp}')



    
    