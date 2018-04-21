import os

from django.conf import settings
from django.contrib.auth.models import User
from django.db import transaction
from django.db.utils import IntegrityError
from django.urls import reverse
from django.test import Client
from django.test import TestCase

from .models import Category
from .models import LogItem
from .models import Task


c = Client()


class InitialTests(TestCase):

    def test_base_dir(self):
        base_dir = os.path.join(os.getcwd(), 'website')
        self.assertEqual(base_dir, settings.BASE_DIR)

    def test_jinja_views_templates(self):
        response = c.get(reverse('dev-test-view'))
        content = str(response.content)
        self.assertEqual(response.status_code, 200)
        self.assertIn('Dev Test View', content)


class ModelTests(TestCase):

    def setUp(self):
        u = User.objects.create_user(
            username='test-user',
            email='test-user@example.com',
            password='test-user'
        )

    def test_create_categories_and_tasks(self):
        task01 = Task(name='My First Task')
        task01.save()

        # Task names are unique (case-sensitive).
        task02 = Task(name='My First Task')
        with transaction.atomic():
            self.assertRaises(IntegrityError, task02.save)
        task02.name = 'My Second Task'
        task02.save()

        category01 = Category(name='Category 1')
        category01.save()

        # Category names are also unique (case-insensitive).
        category02 = Category(name='Category 1')
        with transaction.atomic():
            self.assertRaises(IntegrityError, category02.save)
        category02.name = 'Category 2'
        category02.save()

        task01.categories.add(category01)
        task01.categories.add(category02)
        task02.categories.add(category02)

        self.assertEqual(category02.tasks.count(), 2)
        self.assertEqual(category01.tasks.count(), 1)
        self.assertEqual(task01.categories.count(), 2)
        self.assertEqual(task02.categories.count(), 1)






