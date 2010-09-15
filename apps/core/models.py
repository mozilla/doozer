from django.db import models

import caching.base


# Our apps should subclass ManagerBase instead of models.Manager or
# caching.base.CachingManager directly.
ManagerBase = caching.base.CachingManager


class ModelBase(caching.base.CachingMixin, models.Model):
    """
    Base class for doozer models to abstract some common features.

    * Caching.
    """

    objects = ManagerBase()
    uncached = models.Manager()

    class Meta:
        abstract = True


class TimestampMixin(models.Model):
    """Mixin to add created and updated fields."""
    created = models.DateTimeField(db_index=True, auto_now_add=True)
    updated = models.DateTimeField(db_index=True, auto_now=True)

    class Meta(object):
        abstract = True
