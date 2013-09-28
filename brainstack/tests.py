from django.core.urlresolvers import reverse
from django_webtest import WebTest


class SmokeTest(WebTest):

    def test_can_see_hello(self):
        response = self.app.get(reverse('hello'))
        self.assertEqual(200, response.status_int)
        self.fail('as expected; seems that everything works fine')
