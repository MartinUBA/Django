from django.shortcuts import render
from blog.models import Post, Categoria # importo modelo de post y categoria
from django.contrib.auth.views import LogoutView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required
def blog (request):
    posts=Post.objects.all() #que importe todos los post
    return render(request,"blog/blog.html",{"posts": posts})

def categoria (request, categoria_id):

    categoria= Categoria.objects.get(id=categoria_id)
    posts=Post.objects.filter(categorias=categoria)
    return render(request, "blog/categoria.html",{'categoria': categoria, "posts": posts})

