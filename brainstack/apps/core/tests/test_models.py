from unittest import TestCase


class ProjectTestCase(TestCase):

    def test_can_save(self):
        self.assertFalse(Projects.objects.all().exists())
        Project.objects.create()
        self.assertTrue(Project.objects.all().exists())
