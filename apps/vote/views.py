from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseBadRequest
from django.shortcuts import get_object_or_404
from django.views.decorators.http import require_POST

from core.template import render
from games.models import Game
from vote.forms import VoteForm
from vote.models import Ballot, Vote


@login_required
def ballot(request):
    """Display the list of games this user can vote on."""
    ballot = Ballot.get_or_create(request.user)

    return render(request, 'vote/ballot.html', {'ballot': ballot})


@login_required
@require_POST
def vote(request):
    """Create or update a game rating.

    The game must be in the user's ballot.

    """

    ballot = get_object_or_404(Ballot, creator=request.user)

    form = VoteForm(request.POST)

    if form.is_valid():
        game = get_object_or_404(Game, pk=form.cleaned_data['game'].id)
        if not game in ballot.get_games():
            return HttpResponseBadRequest(mimetype='application/json')
        vote, created = Vote.objects.get_or_create(creator=request.user,
                                                   game=game)
        vote.score = form.cleaned_data['score']
        vote.save()
        return HttpResponse(mimetype='application/json')
    return HttpResponseBadRequest(mimetype='application/json')
