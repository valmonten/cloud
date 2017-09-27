# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect

# Create your views here.
def index(request):
    return render(request, 'words/index.html')
def add(request):
    if not request.session.get('word'):
        request.session['word'] = []
    if not request.session.get('color'):
        request.session['color']= []

    if request.POST.get('word'):
        # request.session['word'].append({'word':request.POST['word'],'color':)
        if request.POST['color']=="Red":
            if request.POST.get('big'):
                request.session['color']="red1"
            else:
                request.session['color']="red2"
        elif request.POST['color']=="Green":
            if request.POST.get('big'):
                request.session['color']="green1"
            else:
                request.session['color']="green2"
        else:
            if request.POST.get('big'):
                request.session['color']="blue1"
            else:
                request.session['color']="blue2"
        request.session['word'].append({'word':request.POST['word'],'color': request.session['color']})

    print request.POST['color']
    print request.session['word']
    return redirect ('/')
def clear(request):
    if request.session.get('word'):
        del request.session['word']
    if request.session.get('color'):
        del request.session ['color']
    return redirect ('/')