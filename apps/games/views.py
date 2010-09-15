from django.contrib.auth.decorators import login_required
from django.core.context_processors import csrf
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render_to_response

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

            # TODO(james) Redirect to Success page

        c.update({'form': form})

        return render_to_response('games/create.html', c)

    return render_to_response('games/create.html', c)


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
            c.update({'success': True})

        return render_to_response('games/edit.html', c)

    form = GameForm(instance=game)
    c.update({'form': form})
    return render_to_response('games/edit.html', c)


@login_required
def delete(request, game_id):
    """Delete an existing game."""


def view(request, game_id):
    """View one game."""
    game = get_object_or_404(Game, id=game_id)
    return render_to_response('games/view.html', {'game': game})


def view_list(request):
    """View a list of games."""
    # TODO(james) Paginate
    games = Game.objects.filter(is_approved=True)
    return render_to_response('games/list.html', {'games': games})
