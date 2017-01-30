from django.template.loader import render_to_string
from django.core.urlresolvers import resolve
from django.http import HttpRequest
from django.test import TestCase

from lists.views import home_page


class SmokeTest(TestCase):

    def test_root_url_resolvers_to_home_page_view(self):
        found = resolve('/')
        self.assertEqual(found.func, home_page)
    
    def test_home_page_returns_correct_html(self):
        request = HttpRequest()
        response = home_page(request)
        expected_html = render_to_string('home.html')
        self.assertIn(b'<title>To-Do lists</title>', response.content)
        self.assertEqual(response.content.decode(), expected_html) 
