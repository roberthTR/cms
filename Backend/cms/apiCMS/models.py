from django.db import models

# Crear los modelos.

class Cliente(models.Model): #falta editar _ str
    
    nombre = models.CharField(max_length=100)
    correo = models.CharField(max_length=100)
    contraseña = models.CharField(max_length=100)
    def __str__(self):
        return self.nombre+" - "+self.nombre
    
class TipoContenido(models.Model): #falta editar _ str
    
    titulo = models.CharField(max_length=100)
    descripcion = models.CharField(max_length=300)
    autor = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    fechaPubli = models.DateField(editable=...)
    def __str__(self):
        return self.titulo+" - "+str(self.autor)
    
class SistemaCMS(models.Model):
    nombre = models.CharField(max_length=100)
    contenido= models.ForeignKey(TipoContenido, on_delete=models.CASCADE)
    def __str__(self):
        return self.nombre
