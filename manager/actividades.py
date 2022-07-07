from datetime import datetime
from datetime import timedelta
import math

from .models import Spring, SpringConfiguration, Activity


class Managment_activities:

    def __init__(self, spring, name, ut, type, project_phase):
        self.spring = spring
        self.name = name
        self.ut = ut
        self.type = type
        self.project_phase = project_phase


    def get_start_date_spring(self):
        spring = Spring.objects.get(pk=self.spring)

        return spring.start_date

    def get_hours_developer(self):
        """
        Obtiene las horas que va a trabajar el desarrollador en el spring
        """
        spring_hours = SpringConfiguration.objects.get(pk=self.spring)
        spring_hours_developer = spring_hours.working_hours

        return spring_hours_developer

    def get_activities(self):
        """ 
        Obtiene todas las actividades del spring
        """
        activities = Activity.objects.filter(spring=self.spring)

        return activities
    
    def hours_to_days(self):
        """ Convert the hours of a activity in days

        Returns:
            int or float: days 
        """
        days = self.ut / self.get_hours_developer()
        return days
    
    def days_and_hours(self):
        """ Convert the decimal part of a day to hours

        Returns:
            int : hours
            int: days
        """
        days = self.hours_to_days()
        hours, days = math.modf(days)
        
        if hours != 0:
            hours = hours * self.get_hours_developer()
       
        
        return hours

    def get_accumlated_hours(self):
        actividades = self.get_activities()
        horas_acumuladas = 0

        for actividad in actividades:
            horas_acumuladas = horas_acumuladas + actividad.ut
        
        return horas_acumuladas

    def get_horas_acumuladas_a_dias(self):
        horas_acumuladas = self.get_accumlated_hours() / self.get_hours_developer()

        return horas_acumuladas
        
    
    def cacula_fecha_inicio(self):
        fecha_inicio_spring = self.get_start_date_spring()
        horas_acumuladas_dias = self.get_horas_acumuladas_a_dias()
        
        fecha_inicio_actividad = fecha_inicio_spring + timedelta(days=horas_acumuladas_dias)
        
        return fecha_inicio_actividad


    
    def calcula_fecha_fin(self, fecha_inicio):
        """ Calculate the end date from days hours

        Returns:
            date: end date of activity
        """
        dias_actividad = self.hours_to_days()
        dias_acumulados = self.get_horas_acumuladas_a_dias()

        dias_totales = dias_actividad + dias_acumulados
        print('DIAS TOTALES: ', dias_totales)
        if fecha_inicio != None:
            end_date = fecha_inicio + timedelta(days=dias_actividad)
       
        return end_date

