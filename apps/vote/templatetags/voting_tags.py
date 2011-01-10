from django import template

from templatetag_sugar.register import tag
from templatetag_sugar.parser import Constant, Variable, Optional, Name

from vote.models import Vote


register = template.Library()


@tag(register, [Constant("for"), Variable(), Variable(),
     Optional([Constant("as"), Name()])])
def vote_score(context, user, game, asvar=None):
    try:
        score = Vote.objects.get(creator=user, game=game).score
    except Vote.DoesNotExist:
        score = 0
    if asvar:
        context[asvar] = score
        return ""
    else:
        return score
