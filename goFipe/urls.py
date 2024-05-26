"""
URL configuration for goFipe project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from core import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('load_marcas/', views.load_marcas, name='load_marcas'),
    path('tabela_final/', views.tabela_final, name='tabela_final'),
    path('load_veiculos/', views.load_veiculos, name='load_veiculos'),
    path('load_anos/', views.load_anos, name='load_anos'),
    path('load_versoes/', views.load_versoes, name='load_versoes'),
    path('criar_grafico/', views.criar_grafico, name='criar_grafico'),
]
