import hashlib

from django.db import models
from django.utils.translation import ugettext as _
from django.contrib.auth.models import User


class Participant(models.Model):
    user = models.ForeignKey(User, verbose_name=_('User'))

    def __unicode__(self):
        return self.user.username


class Project(models.Model):
    title = models.CharField(_('title'), max_length=255)
    description = models.TextField(_('description'), blank=True, null=True)
    link = models.CharField(_('link'), max_length=255)
    owner = models.ForeignKey(Participant, blank=True, null=True)

    def __unicode__(self):
        return self.title

    def save(self, *args, **kwargs):
        self.link = hashlib.md5(self.title).hexdigest()
        super(Project, self).save(*args, **kwargs)


class Task(models.Model):
    title = models.CharField(_('title'), max_length=255)
    number = models.PositiveIntegerField(_('number'))
    project = models.ForeignKey(Project, verbose_name=_('project'))
    estimate = models.IntegerField(_('estimate'), blank=True, null=True,
        help_text=_('in minutes'))
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    start_date_time = models.DateTimeField(blank=True, null=True)
    executor = models.ForeignKey(Participant, blank=True, null=True)

    def __unicode__(self):
        return self.title
