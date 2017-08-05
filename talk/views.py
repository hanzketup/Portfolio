# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

def list(request):

    return render(request, 'talk/list.html')

def item(request):

    return render(request, 'talk/single.html')