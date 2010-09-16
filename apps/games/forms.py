from django import forms

from games.models import Game, Screenshot


class GameForm(forms.ModelForm):
    class Meta(object):
        model = Game
        fields = ('name', 'description', 'url', 'source', 'resources')


class ScreenshotForm(forms.ModelForm):
    class Meta(object):
        model = Screenshot
        fields = ('file',)
