from django.test import TestCase
from django.core.urlresolvers import resolve
from lists.views import home_page #1
from django.http import HttpRequest

class HomePageTest(TestCase):

    def test_root_url_resolves_to_home_page_view(self):
        found = resolve('/') #2
        self.assertEqual(found.func,home_page) #check root is the homepage

    def test_home_page_returns_correct_html(self):
        request = HttpRequest() #httpreq object, dgnao will see whe users asks page
        response = home_page(request)
        self.assertTrue(response.content.startswith(b'<html>'))
        self.assertIn(b'<title>To-Do lists</title>',response.content)
        self.assertTrue(response.content.endswith(b'</html>'))
