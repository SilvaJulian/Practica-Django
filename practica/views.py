# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.http import HttpResponse
import datetime

HTML = """
<!DOCTYPE html>
<html lang="es">
<head>
<meta http­equiv="content­type" content="text/html;  charset=utf­8">
<meta name="robots" content="NONE,NOARCHIVE">
<title>Hola mundo</title>
<style type="text/css">
html * { padding:0; margin:0; }
body * { padding:10px 20px; }
body * * { padding:0; }
body { font:small sans­serif; }
body>div { border­bottom:1px solid #ddd; }
h1 { font­weight:normal; }
#summary { background: #e0ebff; }
</style>
</head>
<body>
<div id="summary">
<h1>¡Hola Mundo!</h1>
</div>
</body></html> """

def hola(request):
    return HttpResponse(HTML)

def fecha_actual(request):
    ahora=datetime.datetime.now()
    return render(request,'fecha_actual.html',{'fecha_actual':ahora})

def horas_adelante(request, horas):
    try:
        horas = int(horas)
    except ValueError:
        raise Http404()
    dt = datetime.datetime.now() + datetime.timedelta(hours=horas)
    return render(request, 'horas_adelante.html', {'hora_siguiente': dt, 'horas': horas })

def atributos_meta(request):
    valor = request.META.items()
    valor.sort()
    return render(request,'atributos_meta.html',{'valor':valor})