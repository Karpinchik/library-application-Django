
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from app.views import base_list, list_books, redaction_book

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', base_list, name='base_list'),
    path('list_books/<int:pk>/', list_books, name='list_books'),
    path('redaction_book/', redaction_book, name='redaction_book'),

]
