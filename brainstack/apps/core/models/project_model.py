import hashlib

from django.db import models
from django.utils.translation import ugettext as _

from core.choices import ROLE
from .user_profile_model import UserProfile


class Project(models.Model):
    class Meta:
        app_label = 'core'

    title = models.CharField(_('title'), max_length=255)
    description = models.TextField(_('description'), blank=True, null=True)
    _hash = models.CharField(_('hash'), max_length=255, blank=True, null=True)

    @property
    def hash(self):
        return self._hash

    participation = models.ManyToManyField(
        UserProfile, through='Participation',
        related_name='projects', blank=True, null=True)

    def __unicode__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.pk and self.title:
            self._hash = hashlib.md5(self.title).hexdigest()
        super(Project, self).save(*args, **kwargs)

    @property
    def owner(self):
        return self.participants.filter(role=ROLE.OWNER)
