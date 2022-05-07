from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns = [
    

    path('',views.blog, name="Blog"),
    path ('categoria/<int:categoria_id>/', views.categoria, name="categoria"),
    
]

