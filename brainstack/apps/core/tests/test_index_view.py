from django.core.urlresolvers import reverse
from django_webtest import WebTest


class MainPageTest(WebTest):

    def test_can_see_main_page(self):
        response = self.app.get(reverse('home'))
        self.assertTemplateUsed('index.html')
