# -*- coding: utf-8 -*-
"""
URLs for the meta_forms app
"""

from django.urls import path, re_path

from meta_dados_rio.meta_forms import views

appname = "shortener"

urlpatterns = [
    path("", views.home_view, name="home"),
]
