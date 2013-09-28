import hashlib

from django.db import models
from django.utils.translation import ugettext as _
from django.contrib.auth.models import User

from .utils import Enumeration




class Project(models.Model):
    title = models.CharField(_('title'), max_length=255)
    description = models.TextField(_('description'), blank=True, null=True)
    _hash = models.CharField(_('hash'), max_length=255, blank=True, null=True)

    @property
    def hash(self):
        return self._hash

    participants = models.ManyToManyField(User, through='Participant',
        related_name='projects', blank=True, null=True)

    def __unicode__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.pk and self.title:
            self._hash = hashlib.md5(self.title).hexdigest()
        super(Project, self).save(*args, **kwargs)


class Task(models.Model):
    class Meta:
        uniquer_together = (
            'project_id', 'number'
        )
        ordering = ['priority']

    PRIORITIES = Enumeration([
        (1, 'HIGH', _('High')),
        (2, 'NORMAL', _('Normal')),
        (3, 'LOW', _('Low')),
        (4, 'SOMEDAY', _('Someday')),
        ])

    title = models.CharField(_('title'), max_length=255)
    number = models.PositiveIntegerField(_('number'), )
    project = models.ForeignKey(Project, related_name='tasks', verbose_name=_('project'))
    estimate = models.IntegerField(_('estimate'), blank=True, null=True,
        help_text=_('in minutes'))
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    start_date_time = models.DateTimeField(blank=True, null=True)
    executor = models.ForeignKey(Participant, blank=True, null=True)
    priority = models.PositiveIntegerField(_('priority'), choices=PRIORITIES)
    created_by = models.ForeignKey(User, through='Participant')

    def __unicode__(self):
        return self.title

    def save(self, *args, **kwargs):
        # FIXME: seems there will be a problem
        self.number = self.project.tasks.count() + 1
        super(Task, self).save(*args, **kwargs)
