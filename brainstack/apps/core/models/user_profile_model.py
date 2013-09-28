from django.contrib.auth.models import User


class UserProfile(User):
    class Meta:
        app_label = 'core'
