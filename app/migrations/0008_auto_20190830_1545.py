# Generated by Django 2.0.5 on 2019-08-30 12:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0007_auto_20190823_1348'),
    ]

    operations = [
        migrations.AlterField(
            model_name='books',
            name='person',
            field=models.ManyToManyField(related_name='books', to='app.Persons'),
        ),
    ]
