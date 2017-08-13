# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

from talk.models import Post, Pro

def index(request):

    posts = Post.objects.all()[:3]
    pros = Pro.objects.all()[:3]


    snd = {

    "posts":posts,
    "pros":pros,

    }

    return render(request, 'start/index.html', snd)
