# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import Http404

from models import *

def getcat():
    return Cat.objects.all()

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

    r = Pro.objects.filter(isexp=False)

    snd = {

        "title": "My Projects",
        "pro": r,
        "allcat": getcat(),

    }

    return render(request,'talk/projects.html', snd)

def listexp(request):

    r = Pro.objects.filter(isexp=True)

    snd = {

        "title": "Experiments",
        "pro": r,
        "allcat": getcat(),

    }

    return render(request,'talk/projects.html', snd)

def catlist(request, cat):

    q = Cat.objects.filter(title=cat)

    if len(q) == 0:
        raise Http404

    else:
        r = Post.objects.filter(cat=q[0].pk)
        snd = {
            "posts": r,
            "title": cat,
            "allcat": getcat(),
        }

        return render(request, 'talk/list.html', snd)