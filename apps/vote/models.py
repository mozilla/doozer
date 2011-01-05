import json
from random import sample, shuffle

from django.conf import settings
from django.contrib.auth.models import User
from django.db import models

from core.models import ModelBase
from games.models import Game


SCORES = zip(range(0, 5), range(0, 5))


class Ballot(ModelBase):
    """An individual ballot with X random games."""
    creator = models.ForeignKey(User)
    games = models.TextField(blank=True)

    def __unicode__(self):
        return self.creator.username

    def get_games(self):
        ids = json.loads(self.games)
        return Game.objects.filter(pk__in=ids)

    def build_ballot(self):
        """Collect X random games."""
        if not self.games:  # Don't regenerate the ballot.
            ids = Game.objects.filter(is_approved=True).values_list('pk', flat=True)
            ids = sample(ids, min(len(ids), settings.BALLOT_SIZE))
            shuffle(ids)
            self.games = json.dumps(ids)
        return self

    @classmethod
    def get_or_create(cls, user):
        try:
            return cls.objects.get(creator=user)
        except cls.DoesNotExist:
            ballot = Ballot(creator=user)
            ballot.build_ballot().save()
            return ballot


class Vote(ModelBase):
    creator = models.ForeignKey(User)
    game = models.ForeignKey(Game)
    score = models.SmallIntegerField(choices=SCORES)

    def __unicode__(self):
        tup = self.creator.username, self.game.name, self.score
        return u'%s: %s: %s' % tup
