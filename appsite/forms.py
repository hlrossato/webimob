# -*- coding: utf-8 -*-

from django import forms
from datetime import datetime


class FormLogin(forms.Form):

    login = forms.CharField(
        label=u'Login', widget=forms.TextInput(attrs={'placeholder': 'LOGIN'}), 
        required=True
    )
    senha = forms.CharField(
        label=u'Senha', required=True,
        widget=forms.PasswordInput(attrs={'placeholder': 'SENHA'}), 
    )  

    def dados(self):
        return {'campo': self.cleaned_data, 'data': datetime.now()}