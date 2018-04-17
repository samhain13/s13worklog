import os

from django.conf import settings
from django.urls import reverse
from django.test import Client
from django.test import TestCase


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

    def test_validation_errors_logitem(self):
        self.assertEqual(0, 1)  # TODO
