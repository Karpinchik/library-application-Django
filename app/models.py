from django.db import models
from django.conf import settings


class Persons(models.Model):
    
    class Meta():
        verbose_name_plural = 'Читатели'
    
    name = models.CharField(max_length=40, verbose_name='name')
    last_name = models.CharField(max_length=40, verbose_name='last_name')

    def __str__(self):
        return self.name


class Books(models.Model):

    class Meta():
        verbose_name_plural = 'Книги'
        
    title = models.CharField("Название", max_length=40)
    person = models.ManyToManyField('Persons', related_name='books')

    def __str__(self):
        return self.title





