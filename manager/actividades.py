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


    def get_fecha_inicio_spring(self):
        """Obtine la fecha inicio del spring

        Returns:
            date: fecha inicio
        """
        spring = Spring.objects.get(pk=self.spring)

        return spring.start_date

    def get_horas_trabajo_desarrollador(self):
        """Obtiene las horas de trabajo configuradas para el spring

        Returns:
            int: horas
        """
        spring_hours = SpringConfiguration.objects.get(pk=self.spring)
        spring_hours_developer = spring_hours.working_hours

        return spring_hours_developer

    def get_actividades(self):
        """Obtiene todas las actividades del spring

        Returns:
            object: actividades
        """
        activities = Activity.objects.filter(spring=self.spring)

        return activities
    
    def convierte_horas_a_dias(self):
        """Convierte las horas de la actividad en dias

        Returns:
            float: dias
        """
        days = self.ut / self.get_horas_trabajo_desarrollador()
        return days
    
    def convierte_parte_decimal_de_dias_a_horas(self):
        """Convierte la parte decimal de los dias en horas en caso de existir

        Returns:
            horas: int
            dias: int
        """
        days = self.convierte_horas_a_dias()
        hours, days = math.modf(days)
        
        if hours != 0:
            hours = hours * self.get_horas_trabajo_desarrollador()
       
        
        return hours

    def get_horas_acumuladas(self):
        """Obtiene las horas de las actividades registradas en el spring

        Returns:
            int: horas acumuladas
        """
        actividades = self.get_actividades()
        horas_acumuladas = 0

        for actividad in actividades:
            horas_acumuladas = horas_acumuladas + actividad.ut
        
        return horas_acumuladas

    def convierte_horas_acumuladas_a_dias(self):
        """Calculas los dias totales de las horas acumuladas en el spring

        Returns:
            int: dias
        """
        dias_totales = self.get_horas_acumuladas() / self.get_horas_trabajo_desarrollador()

        return dias_totales
        
    def cacula_fecha_inicio_actividad(self):
        """Calcula la fecha inicio para la actividad entrante

        Returns:
            date: fecha inicio para actividad
        """
        fecha_inicio_spring = self.get_fecha_inicio_spring()
        dias_totales = self.convierte_horas_acumuladas_a_dias()
        
        fecha_inicio_actividad = fecha_inicio_spring + timedelta(days=dias_totales)
        
        return fecha_inicio_actividad

    def calcula_fecha_fin_actividad(self, fecha_inicio):
        """ Calculate the end date from days hours

        Returns:
            date: end date of activity
        """
        dias_actividad = self.convierte_horas_a_dias()
        dias_acumulados = self.convierte_horas_acumuladas_a_dias()

        dias_totales = dias_actividad + dias_acumulados
        dias_decimal, dias_entera = math.modf(dias_totales)
        if fecha_inicio != None:
            end_date = fecha_inicio + timedelta(days=dias_totales)
       
        return end_date

