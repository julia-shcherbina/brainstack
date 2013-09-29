from django.core.urlresolvers import reverse

from django_webtest import WebTest

from factories import UserFactory


class TaskAPITestCase(WebTest):

    def test_get_tasks(self):
        assert reverse('api:task-list') == '/api/tasks/', reverse('api:task-list')
        user = UserFactory()
        assert user.id
        response = self.app.get(
            reverse('api:task-list'),
            headers={'X-REQUESTED-WITH': 'XMLHttpRequest'},
        )
        self.assertEqual(200, response.status_code)
