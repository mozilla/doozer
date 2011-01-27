from operator import or_

from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.core.urlresolvers import reverse
from django.db.models import Q
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404

from core.decorators import enabled_or_404
from core.template import render
from games.forms import GameForm, ScreenshotForm
from games.models import Game, Screenshot


@enabled_or_404('ALLOW_SUBMISSIONS')
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

            messages.success(request, "Your game was successfully saved!")
            return HttpResponseRedirect(new_game.get_absolute_url())

    return render(request, 'games/create.html', {'form': form})


@enabled_or_404('ALLOW_EDITING')
@login_required
def edit(request, game_id):
    """Edit an existing game."""
    game = get_object_or_404(Game, creator=request.user, pk=game_id)
    form = GameForm(instance=game)
    room_for_more = game.screenshot_set.count() < settings.SCREENSHOTS_MAX
    screenshot_form = ScreenshotForm()

    c = {'game': game,
         'form': form,
         'room_for_more': room_for_more,
         'screenshot_form': screenshot_form,
        }

    if request.POST:
        form = GameForm(request.POST, instance=game)
        c.update({'form': form})
        if form.is_valid():
            form.save()

            messages.success(request, "Your changes were saved!")
            return HttpResponseRedirect(game.get_absolute_url())

    return render(request, 'games/edit.html', c)


@enabled_or_404('ALLOW_DELETING')
@login_required
def delete(request, game_id):
    """Delete an existing game."""

    game = get_object_or_404(Game, id=game_id, creator=request.user)

    if request.POST:
        msg = 'You have deleted the game "%s".' % game.name
        game.delete()

        messages.success(request, msg)
        return HttpResponseRedirect(reverse('games.view_list'))

    return render(request, 'games/delete.html', {'game': game})


def view(request, game_id, slug=None):
    """View one game. It must be approved or yours."""
    filters = []
    user = request.user if request.user.is_authenticated() else None
    if user and not user.is_superuser:
        filters.append(Q(creator=user))
    if not user or not user.is_superuser:
        filters.append(Q(is_approved=True))

    game = get_object_or_404(Game,
        reduce(or_, filters, Q()),
        id=game_id)
    return render(request, 'games/view.html', {'game': game})


@enabled_or_404('ALLOW_GALLERY')
def view_list(request):
    """View a list of games."""
    # TODO: Paginate.
    filters = []
    user = request.user if request.user.is_authenticated() else None
    if user and not user.is_superuser:
        filters.append(Q(creator=user))
    if not user or not user.is_superuser:
        filters.append(Q(is_approved=True))

    games = Game.objects.filter(reduce(or_, filters, Q())).order_by('name')
    return render(request, 'games/list.html', {'games': games})


@enabled_or_404('ALLOW_GALLERY')
def finalists(request):
    """View the list of finalists."""
    games = (Game.objects.filter(id__in=settings.FINALIST_LIST)
             .order_by('name'))
    return render(request, 'games/finalists.html', {'games': games})


@login_required
def mine(request):
    """View your own games."""
    games = request.user.game_set.all()
    return render(request, 'games/mine.html', {'games': games})


@login_required
def screenshots(request, game_id):
    """View/edit screenshots for a game."""
    game = get_object_or_404(Game, id=game_id, creator=request.user)
    room_for_more = game.screenshot_set.count() < settings.SCREENSHOTS_MAX
    form = ScreenshotForm()

    game = get_object_or_404(Game, creator=request.user, pk=game_id)
    form = GameForm(instance=game)
    room_for_more = game.screenshot_set.count() < settings.SCREENSHOTS_MAX
    screenshot_form = ScreenshotForm()


    if request.POST and room_for_more:
        screenshot_form = ScreenshotForm(request.POST, request.FILES)
        if screenshot_form.is_valid():
            new_screenshot = screenshot_form.save(commit=False)
            new_screenshot.game = game
            new_screenshot.save()

            messages.success(request, "Your screenshot has been uploaded!")
            return HttpResponseRedirect(reverse('games.edit',
                                                args=[game.id]))
    c = {'game': game,
         'form': form,
         'room_for_more': room_for_more,
         'screenshot_form': screenshot_form,
    }
    return render(request, 'games/edit.html', c)


@login_required
def screenshot_delete(request, game_id, screenshot_id):
    """Delete a screenshot."""
    game = get_object_or_404(Game, id=game_id, creator=request.user)
    screenshot = get_object_or_404(Screenshot, id=screenshot_id, game=game)

    if request.POST:
        msg = 'You have deleted the screenshot %s!' % screenshot
        screenshot.delete()

        messages.success(request, msg)
        return HttpResponseRedirect(reverse('games.screenshots',
                                            args=[game.id]))

    c = {'game': game, 'screenshot': screenshot}
    return render(request, 'games/screenshot_delete.html', c)
