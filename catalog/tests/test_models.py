from django.test import TestCase
from app.models import Persons, Books


class PersonsModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        Persons.objects.create(name='Джон', last_name='Караби')

    def test_name_label(self):
        person = Persons.objects.get(id=1)
        field_lable = person._meta.get_field('name').verbose_name
        self.assertEqual(field_lable, 'name')

    def test_last_name_label(self):
        person = Persons.objects.get(id=1)
        field_lable = person._meta.get_field('last_name').verbose_name
        self.assertEqual(field_lable, 'last_name')

