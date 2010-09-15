from django.conf import settings
from django.db import models
from django.contrib.auth.models import User

from core.models import ModelBase, TimestampMixin


class Game(ModelBase, TimestampMixin):
    """The game model."""
    creator = models.ForeignKey(User)
    name = models.CharField(max_length=255)
    slug = models.SlugField(unique=True)
    description = models.TextField()
    url = models.URLField()
    source = models.URLField(null=True, blank=True)
    resources = models.TextField(null=True, blank=True)
    is_approved = models.NullBooleanField(default=None, blank=True,
                                          db_index=True)
    reviewed_by = models.ForeignKey(User, related_name='reviewed',
                                    null=True, blank=True)

    def __unicode__(self):
        return self.name


class Screenshot(ModelBase, TimestampMixin):
    """A game screenshot."""
    game = models.ForeignKey(Game)
    file = models.ImageField(upload_to=settings.IMAGE_UPLOAD_PATH)

    def __unicode__(self):
        name = self.file.url.split('/')[-1]
        return u'%s: %s' % (self.game, name)

    def get_absolute_url(self):
        return self.file.url
