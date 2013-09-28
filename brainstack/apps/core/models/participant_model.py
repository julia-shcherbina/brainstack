from django.db import models
from django.utils.translation import ugettext as _

from .project_model import Project
from .user_profile_model import UserProfile
from ..choices import ROLE


class Participation(models.Model):
    class Meta:
        app_label = 'core'

    user = models.ForeignKey(UserProfile, verbose_name=_('User'))
    project = models.ForeignKey(Project, verbose_name=_('Project'),
        related_name='participants')
    role = models.PositiveIntegerField(_('role'), choices=ROLE,
        default=ROLE.CONTRIBUTOR)

    def __unicode__(self):
        return self.user.username
