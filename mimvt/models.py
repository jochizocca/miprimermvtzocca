from django.db import models



class familiares(models.Model):
    nombre=models.CharField('nombre',max_length=20)
    apellido=models.CharField('apellido',max_length=20)
    dni=models.IntegerField('dni')
    dia=models.DateTimeField('dia')
    

class direcciones(models.Model):
    calle=models.CharField('calle',max_length=20)
    localidad=models.CharField('localidad',max_length=20)
    cp=models.IntegerField('cp')

class profesiones(models.Model):
    profesion=models.CharField('profesion',max_length=20)
    
