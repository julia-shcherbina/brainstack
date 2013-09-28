from django.utils.translation import ugettext as _

from .utils import Enumeration

PRIORITY = Enumeration([
    (1, 'HIGH', _('High')),
    (2, 'NORMAL', _('Normal')),
    (3, 'LOW', _('Low')),
    (4, 'SOMEDAY', _('Someday')),
])

ROLE = Enumeration([
    (1, 'OWNER', _('Owner')),
    (2, 'CONTRIBUTOR', _('Contributor'))
])
