# -*- coding: utf-8 -*-
from django.http import HttpResponse


def home_view(request):
    return HttpResponse("It works!")
