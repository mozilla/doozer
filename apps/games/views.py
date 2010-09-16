from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.core.context_processors import csrf
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404

from core.template import render
from games.forms import GameForm, ScreenshotForm
from games.models import Game, Screenshot


@login_required
def create(request):
    """Create a new game."""
    c = {}
    c.update(csrf(request))

    if request.POST:
        form = GameForm(request.POST)
        if form.is_valid():
            new_game = form.save(commit=False)
            new_game.creator = request.user
            new_game.save()

            messages.info(request, "Your game was successfully saved!")
            return HttpResponseRedirect(new_game.get_absolute_url())

        c.update({'form': form})

        return render(request, 'games/create.html', c)

    form = GameForm()
    c.update({'form': form})
    return render(request, 'games/create.html', c)


@login_required
def edit(request, game_id):
    """Edit an existing game."""
    game = get_object_or_404(Game, creator=request.user, pk=game_id)
    c = {'game': game, 'success': False}
    c.update(csrf(request))

    if request.POST:
        form = GameForm(request.POST, instance=game)
        c.update({'form': form})
        if form.is_valid():
            form.save()

            messages.info(request, "Your changes were saved!")
            return HttpResponseRedirect(game.get_absolute_url())

        return render(request, 'games/edit.html', c)

    form = GameForm(instance=game)
    c.update({'form': form})
    return render(request, 'games/edit.html', c)


@login_required
def delete(request, game_id):
    """Delete an existing game."""

    game = get_object_or_404(Game, id=game_id, creator=request.user)
    c = {'game': game}

    if request.POST:
        msg = 'You have deleted the game "%s".' % game.name
        game.delete()

        messages.info(request, msg)
        return HttpResponseRedirect(reverse('games.view_list'))

    return render(request, 'games/delete.html', c)


def view(request, game_id, slug=None):
    """View one game."""
    game = get_object_or_404(Game, id=game_id)
    return render(request, 'games/view.html', {'game': game})


def view_list(request):
    """View a list of games."""
    # TODO(james) Paginate
    games = Game.objects.filter(is_approved=True)
    return render(request, 'games/list.html', {'games': games})
