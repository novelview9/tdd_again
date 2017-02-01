import re

from django.template.loader import render_to_string
from django.core.urlresolvers import resolve
from django.http import HttpRequest
from django.test import TestCase

from lists.views import home_page


class SmokeTest(TestCase):

    @staticmethod
    def remove_csrf(html_code):
        csrf_regex = r'<input[^>]+csrfmiddlewaretoken[^>]+>' 
        return re.sub(csrf_regex, '', html_code)

    def test_root_url_resolvers_to_home_page_view(self):
        found = resolve('/')
        self.assertEqual(found.func, home_page)
    
    def test_home_page_returns_correct_html(self):
        request = HttpRequest()
        response = home_page(request)
        get_html = response.content.decode()
        self.assertIn(b'<title>To-Do lists</title>', response.content)
        expected_html = render_to_string('home.html')
        self.assertEqual(self.remove_csrf(get_html), self.remove_csrf(expected_html))

    def test_home_page_can_save_a_POST_request(self):
        request = HttpRequest()
        request.method = "post"
        request.POST["item_text"] = "new to-do item"
        
        response = home_page(request)

        self.assertIn("new to-do item", response.content.decode())
