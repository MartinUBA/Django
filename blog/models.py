from django.db import models
from django.contrib.auth.models import User

# Categorías de las publicaciones dentro del blog
class Categoria (models.Model):
    
    nombre = models.CharField(max_length=50)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name='categoría'
        verbose_name_plural='categorías'
    
    def __str__(self):
        return self.nombre


#Entradas o posteos dentro del blog
class Post (models.Model):

    post = models.CharField(max_length=50)
    contenido= models.CharField(max_length=50)
    # especifico que se guarden las imagenes en la subcarpeta servicios. 
    # El null y el blank es para que sea opcional subir imagen o no en el posteo
    imagen= models.ImageField(upload_to='blog', null=True, blank= True)
    #Defino al autor de los posteos con su respectiva clave foranea. On_delete es para cuando elimino el usuario tmb se eliminan sus post
    autor=models.ForeignKey(User, on_delete=models.CASCADE) 
    categorias=models.ManyToManyField(Categoria)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name='post'
        verbose_name_plural='posts'
    
    def __str__(self):
        return self.post