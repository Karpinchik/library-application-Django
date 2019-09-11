from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.shortcuts import redirect
from app.forms import Pers, NewBook, RenameBook
from app.models import Books, Persons


def base_list(request):
    if request.method == "POST":
        form = Pers(request.POST)
        if form.is_valid():
            form.save()
            userform = Pers
            all_per = Persons.objects.all()
            context = {'form': form, 'per': all_per, 'userform': userform}
            return render(request, 'base_persons.html', context)
    else:
        userform = Pers
        all_per = Persons.objects.all()
        context = {'form': userform, 'per': all_per, 'userform': userform}
        return render(request, 'base_persons.html', context)


def list_books(request, pk):
    if request.method == "POST":
        form = NewBook(request.POST)
        if form.is_valid():
            form = form.save()
            books_by_persons = request.GET.get('books_by_persons', '')
            person = Persons.objects.get(id=books_by_persons)
            items = person.books.all()
            userform = NewBook
            context = {'form': userform, 'items': items}
            return render(request, 'list_books.html', context)
    else:
        all_per = Persons.objects.all()
        form = NewBook
        books_by_persons = request.GET.get('books_by_persons', '')
        person = Persons.objects.get(id=books_by_persons)
        items = person.books.all()
        context = {'form': form, 'all_per': all_per, 'items': items}
        return render(request, 'list_books.html', context)


def redaction_book(request):
    form = RenameBook(request.POST)
    if request.method == 'POST':
        if form.is_valid():
            new = form.cleaned_data['title']
            per = request.GET.get('per', '')
            book = Books.objects.get(id=per)
            book.title = new
            book.save()
            context = {'form': form, 'book': book}
            return render(request, 'redaction_book.html', context)
    else:
        context = {'form': form}
        return render(request, 'redaction_book.html', context)



