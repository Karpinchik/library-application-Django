from django import forms
from django.forms import ModelForm
from .models import Persons, Books


class Pers(ModelForm):
    class Meta:
        model = Persons
        fields = ('name', 'last_name',)


class NewBook(ModelForm):
    class Meta:
        model = Books
        fields = ('title', 'person')


class RenameBook(ModelForm):
    class Meta:
        model = Books
        fields = ('title',)



