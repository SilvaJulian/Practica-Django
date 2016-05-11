# -*- coding: utf-8 -*-
from contactos.forms import FormularioContactos
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.core.mail import send_mail

def contactos(request):
    if request.method == 'POST':
        form=FormularioContactos(request.POST)
        if form.is_valid():
            cd=form.cleaned_data
            send_mail(cd['asunto'],cd['mensaje'],cd.get('email','noreply@example.com'),['rosacartazzo@gmail.com'],)
            return HttpResponseDirect('contactos/gracias')
    else:
        form=FormularioContactos(initial={'asunto':'Adoro tu sitio'})
    return render(request,'formulariocontactos.html',{'form':form})