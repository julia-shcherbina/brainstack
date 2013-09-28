from unittest import TestCase

from django.contrib.auth.models import User

from core.models import Project, Task, Participant


class ProjectTestCase(TestCase):

    def test_can_save(self):
        Project.objects.all().delete()
        self.assertFalse(Project.objects.all().exists())
        Project.objects.create()
        self.assertTrue(Project.objects.all().exists())


class ParticipantTestCase(TestCase):

    def test_can_save(self):
        Participant.objects.all().delete()
        self.assertFalse(Participant.objects.all().exists())
        project = Project.objects.create()
        user = User.objects.create()
        Participant.objects.create(project=project, user=user)
        self.assertTrue(Participant.objects.all().exists())


class TaskTestCase(TestCase):

    def test_can_save(self):
        Task.objects.all().delete()
        self.assertFalse(Task.objects.all().exists())
        user = User.objects.create(username="test")
        project = Project.objects.create()
        participant = Participant.objects.create(project=project, user=user)
        task_first = Task.objects.create(project=project, executor=participant,
            created_by=user)
        task_second = Task.objects.create(project=project, executor=participant,
            created_by=user)
        self.assertTrue(task_first.number == 1)
        self.assertTrue(task_second.number == 2)
