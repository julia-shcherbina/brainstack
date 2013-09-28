from django.db import models
from django.utils.translation import ugettext as _
from django.contrib.auth.models import User

from .utils import Enumeration
from project_model import Project

ROLES = Enumeration([
    (1, 'OWNER', _('Owner')),
    (2, 'CONTRIBUTOR', _('Contributor'))
])


class Participant(models.Model):

    user = models.ForeignKey(User, verbose_name=_('User'))
    project = models.ForeignKey(Project, verbose_name=_('Project'))
    role = models.PositiveIntegerField(_('role'), choices=ROLES)

    def __unicode__(self):
        return self.user.username
