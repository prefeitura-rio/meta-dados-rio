# -*- coding: utf-8 -*-
"""meta_dados_rio URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from django.urls import include, path

from meta_dados_rio.meta_forms.views import home_view
from meta_dados_rio.meta_forms.urls import router

admin.site.site_header = "MetaDadosRio"
admin.site.site_title = "MetaDadosRio"
admin.site.index_title = "Bem-vindo ao portal de metadados do Escritório de Dados Rio"

urlpatterns = [
    path("", home_view),
    path("admin/", admin.site.urls),
    path("api/", include(router.urls)),
]
