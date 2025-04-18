import contextlib

from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class UsersConfig(AppConfig):
    name = "factoryboy_lecture.users"
    verbose_name = _("Users")

    def ready(self):
        with contextlib.suppress(ImportError):
            import factoryboy_lecture.users.signals  # noqa: F401
