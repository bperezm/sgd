from django.db import models


class Proyect(models.Model):
    STATUS_PROYECT = [
        ('Detenido', 'Detenido'),
        ('Desarrollo', 'Desarrollo'),
        ('Finalizado', 'Finalizado'),
    ]

    name = models.CharField('Nombre', max_length=250, unique=True)
    acronym = models.CharField('Siglas', max_length=20, unique=True, blank=True, null=True)
    start_date = models.DateField('Fecha Inicio')
    end_date = models.DateField('Fecha Fin', blank=True, null=True)
    status = models.CharField('Estatus', choices=STATUS_PROYECT, max_length=50)

    class Meta:
        ordering = ('-start_date',)
    

    def __str__(self):
        return self.name



class Spring(models.Model):
    proyect = models.ForeignKey(Proyect, on_delete=models.CASCADE)
    name = models.CharField('Nombre', max_length=100, unique=True)
    start_date = models.DateField('Fecha Inicio')
    end_date = models.DateField('Fecha Fin', blank=True, null=True)
    total_hours = models.FloatField('Total de Horas', blank=True, null=True)

    class Meta:
        ordering = ('-name', '-start_date',)
    

    def __str__(self):
        return self.name


class Developer(models.Model):
    PROGRAMMING_LANGUAGE = [
        ('python', 'Python'),
        ('php', 'PHP'),
        ('.net', '.Net'),
    ]

    name = models.CharField('Nombre', max_length=100)
    email = models.EmailField('Email', max_length=254)
    language = models.CharField('Lenguaje', max_length=50, choices=PROGRAMMING_LANGUAGE)

    class Meta:
        ordering = ('-name',)
    

    def __str__(self):
        return self.name



class SpringConfiguration(models.Model):
    spring = models.ForeignKey(Spring, on_delete=models.CASCADE)
    developer = models.ForeignKey(Developer, on_delete=models.CASCADE)
    working_hours = models.IntegerField('Horas de Trabajo')

    class Meta:
        ordering = ('-spring',)
    

    def __str__(self):
        return self.spring.name


class Activity(models.Model):
    TYPE = (
        ('E', 'Evolutivo'),
        ('C', 'Correctivo'),
    )

    PROJECT_PHASE = (
        ('C', 'Construcción'),
        ('A', 'Analisis'),
        ('P', 'Pruebas'),
    )

    name = models.CharField('Nombre', max_length=250)
    spring = models.ForeignKey(Spring, on_delete=models.CASCADE)
    ut = models.IntegerField('Horas')
    type = models.CharField('Tipo', max_length=1, choices=TYPE)
    project_phase = models.CharField('Fase', max_length=1, choices=PROJECT_PHASE)
    start_date = models.DateField('Fecha Inicio', auto_now=False, auto_now_add=False)
    end_date = models.DateField('Fecha Fin', auto_now=False, auto_now_add=False)


    def __str__(self):
        return self.name
