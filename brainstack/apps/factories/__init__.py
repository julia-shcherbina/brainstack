from uuid import uuid4

import factory
from factory.django import DjangoModelFactory as DFactory

from core.models import Project, Task, UserProfile


class UserFactory(DFactory):
    FACTORY_FOR = UserProfile
    username = factory.Sequence(
        lambda i: 'username{0}@example.com'.format(uuid4())
    )

    @classmethod
    def _prepare(cls, create, **kwargs):
        DEFAULT_PASSWORD = 'password'
        account = super(UserFactory, cls)._prepare(create, **kwargs)
        account.set_password(DEFAULT_PASSWORD)
        account.save()
        return account


class TaskFactory(DFactory):
    FACTORY_FOR = Task
