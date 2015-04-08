from django.test import TestCase
from django.http import HttpRequest
from django.template.loader import render_to_string
from lists.views import home_page

# Create your tests here.
class HomePageViewTest(TestCase):

	# def test_home_page_returns_correct_html(self):
	# 	request = HttpRequest()
	# 	response = home_page(request)
	# 	self.assertTrue(response.content.startswith(b'<html>'))
	# 	self.assertIn('<title>To-Do lists</title>', response.content.decode('utf8'))
	# 	self.assertTrue(response.content.strip().endswith(b'</html>'))

	def test_home_page_returns_correct_html(self):
		request = HttpRequest()
		response = home_page(request)
		expected_content = render_to_string('home.html')
		self.assertEqual(response.content.decode(), expected_content)
