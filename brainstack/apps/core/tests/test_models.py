from unittest import TestCase

from core.models import Project, Task, Participation, UserProfile


class ProjectTestCase(TestCase):

    def test_can_save(self):
        Project.objects.all().delete()
        self.assertFalse(Project.objects.all().exists())
        Project.objects.create()
        self.assertTrue(Project.objects.all().exists())


class ParticipationTestCase(TestCase):

    def test_can_save(self):
        Participation.objects.all().delete()
        self.assertFalse(Participation.objects.all().exists())
        project = Project.objects.create()
        user = UserProfile.objects.create()
        Participation.objects.create(project=project, user=user)
        self.assertTrue(Participation.objects.all().exists())


class TaskTestCase(TestCase):

    def test_can_save(self):
        Task.objects.all().delete()
        self.assertFalse(Task.objects.all().exists())
        user = UserProfile.objects.create(username="test")
        project = Project.objects.create()
        participant = Participation.objects.create(project=project, user=user)
        task_first = Task.objects.create(project=project, executor=participant,
            created_by=user)
        task_second = Task.objects.create(project=project, executor=participant,
            created_by=user)
        self.assertTrue(task_first.number == 1)
        self.assertTrue(task_second.number == 2)
