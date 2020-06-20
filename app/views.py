# -*- encoding: utf-8 -*-
"""
License: MIT
Copyright (c) 2019 - present AppSeed.us
"""
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
from django.template import loader
from django.http import HttpResponse, JsonResponse
from django import template

from backand.Controller import controller
from backand.Controller import utils

@login_required(login_url="/login/")
def index(request):
    context = load_context(request)
    return render(request, "index.html", context)

@login_required(login_url="/login/")
def pages(request):
    context = load_context(request)



    # All resource paths end in .html.
    # Pick out the html file name from the url. And load that template.
    try:
        
        load_template = request.path.split('/')[-1]
        html_template = loader.get_template( load_template )
        return HttpResponse(html_template.render(context, request))
        
    except template.TemplateDoesNotExist:

        html_template = loader.get_template( 'error-404.html' )
        return HttpResponse(html_template.render(context, request))

    except:
    
        html_template = loader.get_template( 'error-500.html' )
        return HttpResponse(html_template.render(context, request))


def load_context(request):
    context = controller.MenuController().__dict__ # Menu

    if request.GET.get('type') == 'tavolo':  # pagina tavoli
        codice_tavolo = request.GET.get('codice_tavolo')
        context.update(controller.TavoloController.load(codice_tavolo))


    return context




@csrf_exempt
@login_required(login_url="/login/")
@utils.JSON_to_JS
def aggiungi_piatto(request):
    controller.TavoloController.aggiungi_piatto(request.POST)
    return 'Piatto aggiunto correttamente'

