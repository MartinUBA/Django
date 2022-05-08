from django.urls import path

from ProyectoWebApp import views
from django.conf import settings 
from django.conf.urls.static import static 
from django.contrib.auth.views import LogoutView


urlpatterns = [
    
    path('',views.home, name="Home"),
    path('tienda',views.tienda, name="Tienda"),
    path('contacto',views.contacto, name="Contacto"),
    path('covid',views.covid, name="Covid"),
    path('login', views.login_request, name= 'Login'),
    path('register', views.register, name= 'Register'),
    path('logout',LogoutView.as_view(template_name='ProyectoWebApp/logout.html'), name='Logout'),
]

urlpatterns+= static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)