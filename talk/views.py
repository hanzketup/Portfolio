# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

from models import *
from funcs import *

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