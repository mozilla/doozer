from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.core.urlresolvers import reverse
from django.db.models import Q
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404

from core.template import render
from games.forms import GameForm, ScreenshotForm
from games.models import Game, Screenshot


@login_required
def create(request):
    """Create a new game."""
    form = GameForm()

    if request.POST:
        form = GameForm(request.POST)
        if form.is_valid():
            new_game = form.save(commit=False)
            new_game.creator = request.user
            new_game.save()

            messages.info(request, "Your game was successfully saved!")
            return HttpResponseRedirect(new_game.get_absolute_url())

    return render(request, 'games/create.html', {'form': form})


@login_required
def edit(request, game_id):
    """Edit an existing game."""
    game = get_object_or_404(Game, creator=request.user, pk=game_id)
    form = GameForm(instance=game)
    c = {'game': game, 'form': form}

    if request.POST:
        form = GameForm(request.POST, instance=game)
        c.update({'form': form})
        if form.is_valid():
            form.save()

            messages.info(request, "Your changes were saved!")
            return HttpResponseRedirect(game.get_absolute_url())

    return render(request, 'games/edit.html', c)


@login_required
def delete(request, game_id):
    """Delete an existing game."""

    game = get_object_or_404(Game, id=game_id, creator=request.user)

    if request.POST:
        msg = 'You have deleted the game "%s".' % game.name
        game.delete()

        messages.info(request, msg)
        return HttpResponseRedirect(reverse('games.view_list'))

    return render(request, 'games/delete.html', {'game': game})


def view(request, game_id, slug=None):
    """View one game. It must be approved or yours."""
    user = request.user if request.user.is_authenticated() else None
    game = get_object_or_404(Game,
        Q(is_approved=True) | Q(creator=user),
        id=game_id)
    return render(request, 'games/view.html', {'game': game})


def view_list(request):
    """View a list of games."""
    # TODO(james) Paginate
    games = Game.objects.filter(is_approved=True)
    return render(request, 'games/list.html', {'games': games})


@login_required
def screenshots(request, game_id):
    """View/edit screenshots for a game."""
    game = get_object_or_404(Game, id=game_id, creator=request.user)
    form = ScreenshotForm()

    if request.POST:
        form = ScreenshotForm(request.POST, request.FILES)
        if form.is_valid():
            up_file = request.FILES['file']
            new_screenshot = form.save(commit=False)
            new_screenshot.game = game
            new_screenshot.save()

            messages.info(request, "Your screenshot has been uploaded!")
            return HttpResponseRedirect(reverse('games.screenshots',
                                                args=[game.id]))

    c = {'game': game, 'form': form}
    return render(request, 'games/screenshots.html', c)


@login_required
def screenshot_delete(request, game_id, screenshot_id):
    """Delete a screenshot."""
    game = get_object_or_404(Game, id=game_id, creator=request.user)
    screenshot = get_object_or_404(Screenshot, id=screenshot_id, game=game)

    if request.POST:
        msg = 'You have deleted the screenshot %s!' % screenshot
        screenshot.delete()

        messages.warning(request, msg)
        return HttpResponseRedirect(reverse('games.screenshots',
                                            args=[game.id]))

    c = {'game': game, 'screenshot': screenshot}
    return render(request, 'games/screenshot_delete.html', c)
