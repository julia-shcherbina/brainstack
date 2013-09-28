from django.core.urlresolvers import reverse

from django_webtest import WebTest


class TaskAPITestCase(WebTest):

    def test_get_tasks(self):
        response = self.app.get(
            reverse('api:task-list'),
            headers={'X-REQUESTED-WITH': 'XMLHttpRequest'},
        )
        self.assertEqual(200, response.status_code)
