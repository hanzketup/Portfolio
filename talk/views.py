# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

from models import *
from funcs import *

#blog views

def list(request):

    r = Post.objects.all()

    snd = {
        "posts":r,
        "title":"Latest posts",
        "allcat": getcat(),

    }

    return render(request, 'talk/list.html', snd)

def resolv(request, pk):

    r = Post.objects.get(pk=pk)

    snd = {
        "title": r.title,
        "date": r.date,
        "short": r.short,
        "content": r.content,
        "cat": str(r.cat.all()[0]),
        "allcat":getcat(),

    }

    return render(request, 'talk/single.html', snd)

#project views

def listproject(request):

    r = Pro.objects.all()

    snd = {

        "title": "My Projects",
        "pro": r,
        "allcat": getcat(),

    }

    return render(request,'talk/projects.html', snd)