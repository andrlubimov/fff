from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

from ray import models


def page1view(request):
    template = loader.get_template('1page.html')
    context = {'1': '1'}

    return HttpResponse(template.render(context, request))


def page2view(request):
    template = loader.get_template('2page.html')
    context = {'1': '1'}

    return HttpResponse(template.render(context, request))


def page3view(request):
    template = loader.get_template('3page.html')
    context = {'1': '1'}

    return HttpResponse(template.render(context, request))


def page4view(request):
    template = loader.get_template('4page.html')
    data = models.uslugi.objects.all()
    list = []
    for i in data:
        list.append(i)

    context = {'data': list}

    return HttpResponse(template.render(context, request))


def page5view(request):
    template = loader.get_template('5page.html')
    context = {'1': '1'}

    return HttpResponse(template.render(context, request))

# Create your views here.
