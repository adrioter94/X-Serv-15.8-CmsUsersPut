from django.shortcuts import render
from models import Page
from django.http import HttpResponse, HttpResponseNotFound

# Create your views here.


def processCMS_Users(request, recurso):

    salida = ""
    if request.user.is_authenticated():
        salida += "Logged in as " + request.user.username + ". "
        salida += "<a href='/admin/logout/'>Logout</a><br>"
    else:
        salida += "Not logged in."
        salida += "<a href='/admin/login/'>Login</a><br>"

    if request.method == "GET":
        try:
            fila = Page.objects.get(name=recurso)
            return HttpResponse(salida + "<br>" + fila.page)
        except Page.DoesNotExist:
            return HttpResponseNotFound(salida +
                                        "<br>Page not found: /%s" % recurso)
    elif request.method == "PUT":
        if request.user.is_authenticated():
            try:
                cuerpo = request.body
                fila = Page.objects.create(name=recurso, page=cuerpo)
                fila.save()
                return HttpResponse("Nueva fila")
            except:
                return HttpResponseNotFound("Error")
        else:
            return HttpResponseNotFound("No puedes modificarlo\
                                         si no estas auntetificado")
