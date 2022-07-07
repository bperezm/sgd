from tkinter import Widget
from django import forms


class ProyectForm(forms.Form):
    STATUS_PROYECT = [
        ('Detenido', 'Detenido'),
        ('Desarrollo', 'Desarrollo'),
        ('Finalizado', 'Finalizado'),
    ]

   

    name = forms.CharField(label='Nombre', max_length=250, widget=forms.TextInput(attrs={'class':'form-control'}))
    acronym = forms.CharField(label='Siglas', max_length=20, required=False, widget=forms.TextInput(attrs={'class':'form-control'}))
    start_date = forms.DateField(label='Fecha Inicio', widget=forms.DateInput(attrs={'class':'form-control'}))
    end_date = forms.DateField(label='Fecha Fin', widget=forms.DateInput(attrs={'class':'form-control'}))
    status = forms.CharField(label='Estatus', widget=forms.Select(attrs={'class':'form-control'}, choices=STATUS_PROYECT ))


class ActivityForm(forms.Form):


    TYPE = (
        ('E', 'Evolutivo'),
        ('C', 'Correctivo'),
    )

    PROJECT_PHASE = (
        ('C', 'Construcción'),
        ('A', 'Analisis'),
        ('P', 'Pruebas'),
    )

    name = forms.CharField(label='Nombre', max_length=250, required=True, widget=forms.TextInput(attrs={'class':'form-control'}))
    ut = forms.IntegerField(label='Horas', required=True, widget=forms.NumberInput(attrs={'class':'form-control'}))
    type = forms.CharField(label='Tipo', max_length=1,  widget=forms.Select(attrs={'class':'form-control'}, choices=TYPE ))
    project_phase = forms.CharField(label='Fase', max_length=1,  widget=forms.Select(attrs={'class':'form-control'}, choices=PROJECT_PHASE ))

