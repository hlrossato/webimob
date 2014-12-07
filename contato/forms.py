# -*- coding: utf-8 -*-

from django import forms
from models import *
from datetime import datetime


class FormContato(forms.ModelForm):

    from captcha.fields import CaptchaField
    captcha = CaptchaField()

    assunto = forms.ModelChoiceField(queryset=Assunto.objects.all(), 
        widget=forms.Select(), required=True, empty_label="ASSUNTO"
    )    
    nome = forms.CharField(
        label=u'Nome', widget=forms.TextInput(attrs={'placeholder': 'NOME'}), 
        required=True
    )
    email = forms.EmailField(
        label=u'Email', widget=forms.TextInput(attrs={'placeholder': 'EMAIL'}), 
        required=True
    )
    telefone = forms.CharField(
        label=u'Email', required=False,
        widget=forms.TextInput(attrs={'placeholder': 'TELEFONE'}), 
    )
    mensagem = forms.CharField(
        label=u'Email', required=True,
        widget=forms.Textarea(attrs={'placeholder': 'MENSAGEM'}), 
    )

    class Meta:
        model = Contato

    def dados(self):
        return {'campo': self.cleaned_data, 'data': datetime.now()}