from unittest import TestCase

from core.models import Project, Task, Participant

class ProjectTestCase(TestCase):

    def test_can_save(self):
        self.assertFalse(Project.objects.all().exists())
        Project.objects.create()
        self.assertTrue(Project.objects.all().exists())


class TaskTestCase(TestCase):

    def test_can_save(self):
        self.assertFalse(Task.objects.all().exists())
        Task.objects.create()
        self.assertTrue(Task.objects.all().exists())


class ParticipantTestCase(TestCase):

    def test_can_save(self):
        self.assertFalse(Participant.objects.all().exists())
        Participant.objects.create()
        self.assertTrue(Participant.objects.all().exists())
