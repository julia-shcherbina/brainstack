from django.db import models
from django.utils.translation import ugettext as _

class Project(models.Model):
    title = models.CharField(_('title'), max_length=255)
    description = models.TextField(_('description'), blank=True, null=True)
    link = models.CharField(_('link'), max_length=50)

    def __unicode__(self):
        return self.title
