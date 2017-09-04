# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib.auth import authenticate, login, logout

from django.shortcuts import render, redirect

from talk.models import Post, Pro, Cat

from forms import newPost

import datetime

def home(request):

    if request.user.is_authenticated:
        return render(request, "dash/dashBase.html")
    else:
        return redirect('/admin')

def dashlist(request):

    if request.user.is_authenticated:
        r = Post.objects.all()

        snd = {

            'title':'articles/dashboard',
            'posts': r,

        }

        return render(request, "dash/dashList.html", snd)
    else:
        return redirect('/admin')

def dashart(request, pk):

    if request.method == 'POST':
        form = newPost(request.POST)
        if form.is_valid():
            f = form.cleaned_data
            a = Post.objects.get(pk=f['pk'])
            a.title = f['title']
            a.content = f['content']
            a.save()
            return redirect('/dashboard/articles/' + str(a.pk))



    if request.method == 'GET':
        if request.user.is_authenticated:
            r = Post.objects.get(pk=pk)
            c = Cat.objects.all()

            snd = {
                "title": r.title,
                "content": r.content,
                "pk":r.pk,

                "cat": c,
                "titleval": r.title,

            }

            return render(request, 'dash/dashArticle.html', snd)
        else:
            return redirect('/admin')

def dashnew(request):

    if request.method == 'POST':
        form = newPost(request.POST)
        if form.is_valid():
            f = form.cleaned_data
            c = Cat.objects.get(pk=f['cat'])
            a = Post(title=f['title'],content=f['content'], date=datetime.datetime.now().date())
            a.save()
            a.cat.add(c)
            a.save()
            return redirect('/dashboard/articles/' + str(a.pk))

        else:
            return render(request, 'dash/dashErr.html')

    if request.method == 'GET':
        if request.user.is_authenticated:
            c = Cat.objects.all()

            snd = {
                "title": "New",
                "cat": c,

            }

            return render(request, 'dash/dashArticle.html', snd)
        else:
            return redirect('/admin')


def dashout(request):
    logout(request)
    return redirect('/')