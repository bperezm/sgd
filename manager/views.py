from datetime import datetime
from datetime import timedelta
from django.http import HttpResponse
from re import template
import re
from django.shortcuts import render
from django.views.generic import View

from manager.models import Proyect, Spring, Activity
from .forms import ProyectForm, ActivityForm
from .actividades import Managment_activities

class ProyectView(View):

    def get(self, request):

        template_name = 'manager/proyects/list.html'
        proyects = Proyect.objects.all()

        return render(request, template_name, {'proyects':proyects})


class ProyectCreateView(View):

    def get(self, request):
        template_name = 'manager/proyects/create.html'
        form = ProyectForm()
        return render(request, template_name, {'form':form})
    

class SpringsView(View):

    def get(self, request, pk_proyect):
        template_name = 'manager/springs/list.html'
        proyect = Proyect.objects.get(pk=pk_proyect)
        springs = Spring.objects.filter(proyect=proyect)

        return render(request, template_name, {'springs': springs, 'proyect': proyect})


class ActivitiesListView(View):
    def get (self, request, pk_spring):
        template_name = 'manager/activities/list.html'
        activities = Activity.objects.filter(spring=pk_spring)
        context = {'activities': activities, 'spring': pk_spring}
        return render(request, template_name, context )


class ActivityCreateView(View):
    def get(self, request, spring):
        template_name = 'manager/activities/create.html'
        form = ActivityForm()
        context = {'form': form, 'spring': spring}

        return render(request, template_name, context)

    def post(self, request, *args, **kwargs):
        form = ActivityForm(request.POST)

        if form.is_valid():
            spring = request.POST.get('spring_id')
            name = form.cleaned_data['name']
            ut = form.cleaned_data['ut']
            type = form.cleaned_data['type']
            project_phase = form.cleaned_data['project_phase']
            intance_spring = Spring.objects.get(pk=spring)
            validate = Managment_activities(spring, name, ut, type, project_phase)
            validate.get_start_date_spring()

            if len(validate.get_activities()) == 0:
                print('Es la primera actividad')
                return HttpResponse("Se creo la actividad")
            else:
                fecha_inicio_spring = validate.get_start_date_spring()
                print('fecha inicio del spring: {}'.format(fecha_inicio_spring))

                horas_acumuladas_spring = validate.get_accumlated_hours()
                print('Horas acumuladas en el spring {} horas'.format(horas_acumuladas_spring))

                horas_acumuladas_a_dias = validate.get_horas_acumuladas_a_dias()
                print('Las horas acumuladas del spring equivalen a {} dias'.format(horas_acumuladas_a_dias))
                
                print('UT ingresadas {}'.format(ut))

                horas_actividad_a_dias = validate.hours_to_days()
                print('Las ut ingresadas equivalen a: {} dias'.format(horas_actividad_a_dias))

                parte_decimal_a_horas = validate.days_and_hours()
                print('La parte decimal equivale a {} horas'.format(parte_decimal_a_horas))

                fecha_inicio_actividad = validate.cacula_fecha_inicio()
                print('La fecha inicio de la actividad es {}'.format(fecha_inicio_actividad))

                fecha_fin_actividad = validate.calcula_fecha_fin(fecha_inicio_actividad)
                print('La fecha fin de la actividad es {}'.format(fecha_fin_actividad))

                actividad = Activity(name=name, spring=intance_spring, ut=ut, type=type, project_phase=project_phase,start_date=fecha_inicio_actividad, end_date=fecha_fin_actividad )
                actividad.save()

                return HttpResponse("Se creo la actividad")
