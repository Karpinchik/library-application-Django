# Generated by Django 2.0.5 on 2019-08-22 13:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_auto_20190822_1228'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='book',
            options={'verbose_name': 'Книга', 'verbose_name_plural': 'Книги'},
        ),
        migrations.AlterModelOptions(
            name='persons',
            options={'verbose_name': 'Читатель', 'verbose_name_plural': 'Читатели'},
        ),
    ]
