from django.test import TestCase
from django.core.urlresolvers import resolve
from lists.views import home_page #1
from django.http import HttpRequest
from django.template.loader import render_to_string

class HomePageTest(TestCase):

    def test_root_url_resolves_to_home_page_view(self):
        found = resolve('/') #2
        self.assertEqual(found.func,home_page) #check root is the homepage

    def test_home_page_returns_correct_html(self):
        request = HttpRequest() #httpreq object, dgnao will see whe users asks page
        response = home_page(request)
        expected_html = render_to_string('home.html')
        self.assertEqual(response.content.decode(),expected_html)

    def test_home_page_can_save_a_POST_request(self):
        request = HttpRequest()
        request.method = 'POST'
        request.POST['item_text'] = 'A new list item'

        response = home_page(request)
        self.assertIn('A new list item',response.content.decode())
        expected_html = render_to_string('home.html',
                {'new_item_text':'A new list item'})
        self.assertEqual(response.content.decode(),expected_html)
