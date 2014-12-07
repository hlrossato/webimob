# -*- coding: utf-8 -*-

from django import forms
from models import *
from datetime import datetime
from utils import util as U


class FormPreCadastroCliente(forms.ModelForm):

    nome = forms.CharField(
        label=u'Nome', widget=forms.TextInput(attrs={'placeholder': 'NOME *'}), 
        required=True
    )
    email = forms.EmailField(
        label=u'Email', widget=forms.TextInput(attrs={'placeholder': 'EMAIL *'}), 
        required=True
    )
    telefone = forms.CharField(
        label=u'Telefone', 
        widget=forms.TextInput(attrs={'placeholder': 'TELEFONE *'}), required=True
    ) 
    celular = forms.CharField(
        label=u'Celular', required=False,
        widget=forms.TextInput(attrs={'placeholder': 'CELULAR'}), 
    )
    data_nascimento = forms.DateField(
        label=u'Data de Nascimento', required=True,
        widget=forms.DateInput(format=('%d/%m/%Y'), 
            attrs={'placeholder': 'DATA DE NASCIMENTO *'}
        ),
    )   

    class Meta:
        model = PreCadastroCliente

    def dados(self):
        return {'campo': self.cleaned_data, 'data': datetime.now()}


class FormCadastroCliente(forms.ModelForm):

    EMPTY_ESTADOS = (('', u'SELECIONE UM ESTADO *'),)
    EMPTY_PROFISSOES = (('', u'SELECIONE UMA PROFISSÃO *'),)
    EMPTY_PROFISSOES_CONJUGE = (('', u'SELECIONE UMA PROFISSÃO DO CONJUGE'),)
    EMPTY_ESTADO_CIVIL = (('', u'SELECIONE UM ESTADO CIVIL *'),)

    nome = forms.CharField(
        label=u'Nome', widget=forms.TextInput(attrs={'placeholder': 'NOME *'}), 
        required=True
    )
    email = forms.EmailField(
        label=u'Email', widget=forms.TextInput(attrs={'placeholder': 'EMAIL *'}), 
        required=True
    )
    telefone = forms.CharField(
        label=u'Telefone', required=True, 
        widget=forms.TextInput(attrs={'placeholder': 'TELEFONE *'}), 
    ) 
    celular = forms.CharField(
        label=u'Celular', required=False,
        widget=forms.TextInput(attrs={'placeholder': 'CELULAR'}), 
    )
    data_nascimento = forms.DateField(
        label=u'Data de Nascimento', required=True,
        widget=forms.DateInput(format=('%d/%m/%Y'),
            attrs={'placeholder': 'DATA DE NASCIMENTO *'}
        ),
    )
    rg = forms.CharField(
        label='RG', widget=forms.TextInput(attrs={'placeholder': 'RG *'}),
        required=True
    )
    cpf = forms.CharField(
        label='CPF', widget=forms.TextInput(attrs={'placeholder': 'CPF *'}),
        required=True
    )
    endereco = forms.CharField(
        label=u'Endereço', required=True,
        widget=forms.TextInput(attrs={'placeholder': 'ENDEREÇO *'})
    )
    cidade = forms.CharField(
        label='Cidade', widget=forms.TextInput(attrs={'placeholder': 'CIDADE *'}),
        required=True
    )
    estado = forms.ChoiceField(
        choices=EMPTY_ESTADOS + STATE_CHOICES, required=True
    )
    estado_civil = forms.ChoiceField(
        choices=EMPTY_ESTADO_CIVIL + U.ESTADO_CIVIL, required=True
    )
    profissao = forms.ChoiceField(
        choices=EMPTY_PROFISSOES + U.PROFISSOES, required=True
    )
    nome_conjuge = forms.CharField(
        label=u'Nome Conjugê', required=False,
        widget=forms.TextInput(attrs={'placeholder': 'NOME DO CONJUGÊ'})
    )
    endereco_conjuge = forms.CharField(
        label=u'Endereço Conjugê', required=False,
        widget=forms.TextInput(attrs={'placeholder': 'ENDEREÇO DO CONJUGÊ'})
    )
    telefone_conjuge = forms.CharField(
        label=u'Telefone Conjugê', required=False,
        widget=forms.TextInput(attrs={'placeholder': 'TELEFONE DO CONJUGÊ'}), 
    )
    celular_conjuge = forms.CharField(
        label=u'Celular Conjugê', required=False,
        widget=forms.TextInput(attrs={'placeholder': 'CELULAR DO CONJUGÊ'}), 
    )
    data_nascimento_conjuge = forms.DateField(
        label=u'Data de Nascimento Conjugê', required=False,
        widget=forms.DateInput(format=('%d/%m/%Y'),
            attrs={'placeholder': 'DATA DE NASCIMENTO DO CONJUGÊ'}
        ),
    )
    rg_conjuge = forms.CharField(
        label='RG CONJUGÊ', required=False,
        widget=forms.TextInput(attrs={'placeholder': 'RG DO CONJUGÊ'})
    )
    cpf_conjuge = forms.CharField(
        label='CPF CONJUGÊ', required=False,
        widget=forms.TextInput(attrs={'placeholder': 'CPF DO CONJUGÊ'})
    )
    profissao_conjuge = forms.IntegerField(
        widget=forms.Select(choices=EMPTY_PROFISSOES_CONJUGE + U.PROFISSOES),
        required=False,        
    )
    faixa_salarial = forms.CharField(
        label='Faixa Salarial', required=True,
        widget=forms.TextInput(attrs={'placeholder': 'FAIXA SALARIAL *'})
    )
    filhos = forms.BooleanField(
        label=u'Possui Filhos?', required=False
    )
    qtde_filhos = forms.IntegerField(
        label='Qtde Filhos', required=False,
        widget=forms.TextInput(attrs={'placeholder': 'QUANTIDADE DE FILHOS'})
    )

    class Meta:
        model = CadastroCliente

    def dados(self):
        return {'campo': self.cleaned_data, 'data': datetime.now()}
