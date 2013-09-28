from django.db import models
from django.utils.translation import ugettext as _
from django.contrib.auth.models import User

from .project_model import Project
from .participant_model import Participant
from ..choices import PRIORITY


class Task(models.Model):
    class Meta:
        app_label = 'core'
        unique_together = (
            'project', 'number'
        )
        ordering = ['priority']

    title = models.CharField(_('title'), max_length=255)
    number = models.PositiveIntegerField(_('number'), )
    project = models.ForeignKey(
        Project, related_name='tasks', verbose_name=_('project'))
    estimate = models.IntegerField(
        _('estimate'), blank=True, null=True,
        help_text=_('in minutes'))
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    start_date_time = models.DateTimeField(blank=True, null=True)
    executor = models.ForeignKey(Participant, blank=True, null=True)
    priority = models.PositiveIntegerField(_('priority'), choices=PRIORITY,
        default=PRIORITY.NORMAL)
    created_by = models.ForeignKey(User, related_name='created_task')

    def __unicode__(self):
        return self.title

    def save(self, *args, **kwargs):
        # FIXME: seems there will be a problem
        self.number = self.project.tasks.count() + 1
        super(Task, self).save(*args, **kwargs)
