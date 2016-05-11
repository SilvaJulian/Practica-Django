# -*- coding: utf-8 -*-
from django import forms

class FormularioContactos(forms.Form):
    asunto=forms.CharField(max_length=20)
    email=forms.EmailField(required=False, label='Tu correo electronico')
    mensaje=forms.CharField(widget=forms.Textarea)

    def clean_message(self):
        mensaje= self.cleaned_data['mensaje']
        num_words = len(mensaje.split())
        if num_words < 4:
            raise forms.ValidationError("Not enough words!")
        return mensaje